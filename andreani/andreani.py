'''
Implementa los servicios ofrecidos por el webservice de andreani.
'''
import string

from . import validator

import suds.client
import suds.wsse
from suds.bindings import binding
# modifico namespace del envoltorio soap
binding.envns = ('SOAP-ENV', 'http://www.w3.org/2003/05/soap-envelope')


class API(object):

    '''
    Implementa los servicios ofrecidos por el webservice de andreani.
    '''

    DEBUG = False
    _url_staging = "https://www.e-andreani.com/CasaStaging/eCommerce/%s?wsdl"
    _URL = {
        'Staging': {
            'consultar_sucursales': (_url_staging % 'ConsultaSucursales.svc',
                                     'ConsultarSucursales'),
            'cotizar_envio': (_url_staging % 'CotizacionEnvio.svc',
                              'CotizarEnvio'),
            'confirmar_compra': (_url_staging % 'ImposicionRemota.svc',
                                 'ConfirmarCompra'),
            'confirmar_compra_datos_impresion':
                (_url_staging % 'ImposicionRemota.svc',
                 'ConfirmarCompraConRecibo'),
        },
    }

    def __init__(self, username, password, cliente, contrato):
        '''
        Inicializa datos del objeto
        '''
        # guardo token generado como atributo del objeto
        token = suds.wsse.UsernameToken(username, password)
        self.security = suds.wsse.Security()
        self.security.tokens.append(token)
        # numero de cliente
        self.cliente = cliente
        # numero de servicio andreani
        self.contrato = contrato

    def __soap(self, peticion, **kwargs):
        '''
        Realiza la peticion SOAP y devuelve el resultado
        '''
        try:
            # obtengo url del wsdl y nombre de metodo a llamar
            wsdl, metodo = self.__get_wsdl(peticion)
            soap = suds.client.Client(wsdl)
            # configuro content-type de la peticion
            # XXX: es obligatorio para el servidor que el parametro "action"
            # este dentro de la cabecera 'Content-Type'
            metodo = getattr(soap.service, metodo)
            soap.set_options(wsse=self.security,
                             headers={'Content-Type':
                                      'application/soap+xml;charset=utf-8;' +
                                      'action=%s' %
                                      metodo.method.soap.action})
            return metodo(**kwargs)
        except suds.WebFault as e:
            text = e.fault.Reason.Text
            if text == "Codigo postal es invalido":
                raise CodigoPostalInvalido from e
            raise APIError(text) from e

    def consultar_sucursales(self,
                             codigo_postal=None,
                             localidad=None,
                             provincia=None):
        '''
        Devuelve una lista de sucursales Andreani habilitadas para la entrega
        por mostrador.
        '''
        # configuro parametros de la consulta
        if codigo_postal or localidad or provincia:
            consulta = {'CodigoPostal': codigo_postal,
                        'Localidad': localidad,
                        'Provincia': provincia}
        else:
            # XXX: tengo que forzar enviar null porque el webservice lanza una
            # excepcion si el parametro <consulta> no esta en la peticion
            consulta = {'CodigoPostal': suds.null()}
        # realizo la consulta y obtengo el resultado
        r = self.__soap('consultar_sucursales', consulta=consulta)
        # devuelvo lista de sucursales
        return ([self.__to_dict(sucursal) for sucursal in r[0]] if r else [])

    @validator.gt("peso", 0)
    @validator.gt("volumen", 0)
    def cotizar_envio(self, peso, volumen, cp_destino, sucursal_retiro=None):
        '''
        Permite cotizar en línea el costo de un envío.

        args
        --------
        sucursal_retiro -- integer: Código de "Sucursal Andreani" donde el
                                    envío permanecerá en Custodia. Obligatorio
                                    para los Servicios de Retiro en Sucursal
        cp_destino -- string: Obligatorio para los Servicios de Envío a
                              Domicilio
        peso -- float: Expresado en gramos
        volumen -- float: Expresados en centimetros cúbicos
        '''
        # configuro parametros de la peticion
        parametros = {
            'CPDestino': cp_destino,
            'Cliente': self.cliente,
            'Contrato': self.contrato,
            'Peso': peso,
            'SucursalRetiro': sucursal_retiro,
            'Volumen': volumen,
        }
        # obtengo resultado
        response = self.__soap("cotizar_envio", cotizacionEnvio=parametros)
        return self.__to_dict(response) if response else None

    def confirmar_compra(self, **kwargs):
        '''
        Genera un envío en Andreani.

        Asigna un identificador con el cual se va a hacer el seguimiento.
        Luego se debe llamar al WS de Imprimir Constancia para finalizar el
        proceso de Alta del envío.

        params
        -----------------------
        sucursal_retiro -- Integer: Código de "Sucursal Andreani" donde el
                                    envío permanecerá en Custodia. Obligatorio
                                    para los Servicios de Retiro en Sucursal
                                    (valor "sucursal" de la consulta de
                                    sucursales)
        provincia -- String
        localidad -- String
        codigo_postal -- String: Codigo postal del destino
        calle -- String
        numero -- String
        departamento -- String
        piso -- String
        nombre_apellido -- String
        tipo_documento -- String
        numero_documento -- String
        email -- String
        numero_celular -- String
        numero_telefono -- String
        email -- String
        nombre_apellido_alternativo -- String
        numero_transaccion -- String: ID de identificación de envío del Cliente
        detalle_productos_entrega -- String
        detalle_productos_retiro -- String
        peso -- Float: Expresado en Gramos (gr.)
        volumen -- Float: Expresado en Centímetros Cúbicos (cc3.) (No es
                          obligatorio si se usan categorías de peso).
                          Considerar el volumen del envoltorio/Embalaje.
        valor_declarado -- Float: Obligatorio para los Servicios que incluye
                                 seguro en caso de siniestro
        valor_cobrar -- Float: Obligatorio para los Servicio que incluyen
                               Gestión Cobranza (pago contrareembolso)
        sucursal_cliente -- String: Nombre que identifica la sucursal/depósito
                                    del Cliente. Obligatorio para los Servicios
                                    de Retiro en Sucursal Andreani más próxima
                                    a la sucursal/depósito de Cliente
        categoria_distancia -- Integer: Código de categoría para la cotización.
                                        Obligatorio cuando la tarifas del
                                        servicio se cotizan por Categorías de
                                        Distancia
        categoria_facturacion -- Integer: Uso interno
        categoria_peso -- Integer: Código de categoría para la cotización.
                                   Obligatorio cuando la tarifas del servicio
                                   se cotizan por Categorías de Peso. (por ej.
                                   1.- Zapatos, 2.-Indumentaria)
        tarifa -- Decimal: Valor de cotización del envío. Sólo se setea
                           si se consume el servicio web de Cotización.
                           Este valor es de referencia, ya que el sistema
                           recalculará la tarifa junto con el alta.
        '''
        # configuro parametros de la peticion
        parametros = {
            'SucursalRetiro': kwargs.get('sucursal_retiro'),
            'Provincia': kwargs.get('provincia'),
            'Localidad': kwargs.get('localidad'),
            'CodigoPostalDestino': kwargs.get('codigo_postal'),
            'Calle': kwargs.get('calle'),
            'Numero': kwargs.get('numero'),
            'Departamento': kwargs.get('departamento'),
            'Piso': kwargs.get('piso'),
            'NombreApellido': kwargs.get('nombre_apellido'),
            'TipoDocumento': kwargs.get('tipo_documento'),
            'NumeroDocumento': kwargs.get('numero_documento'),
            'Email': kwargs.get('email'),
            'NumeroCelular': kwargs.get('numero_celular'),
            'NumeroTelefono': kwargs.get('numero_telefono'),
            'NombreApellidoAlternativo': kwargs.get(
                'nombre_apellido_alternativo'),
            'NumeroTransaccion': kwargs.get('numero_transaccion'),
            'DetalleProductosEntrega': kwargs.get('detalle_productos_entrega'),
            'DetalleProductosRetiro': kwargs.get('detalle_productos_retiro'),
            'Peso': kwargs.get('peso'),
            'Volumen': kwargs.get('volumen'),
            'ValorDeclarado': kwargs.get('valor_declarado'),
            'ValorACobrar': kwargs.get('valor_cobrar'),
            'Contrato': self.contrato,
            'SucursalCliente': kwargs.get('sucursal_cliente'),
            'CategoriaDistancia': kwargs.get('categoria_distancia'),
            'CategoriaFacturacion': kwargs.get('categoria_facturacion'),
            'CategoriaPeso': kwargs.get('categoria_peso'),
            'Tarifa': kwargs.get('tarifa'),
        }
        # obtengo resultado
        response = self.__soap("confirmar_compra", compra=parametros)
        return self.__to_dict(response) if response else None

    def confirmar_compra_datos_impresion(self, **kwargs):
        '''
        Genera un envío y devuelve todos los datos necesarios para
        que el cliente imprima la etiqueta del bulto.

        A diferencia del Confirmar compra el pedido finaliza el proceso de
        Alta, El uso de este Web Services es recomendado para cliente que
        tienen altas intensivas y un proceso de preparación que
        necesita agilidad

        params
        -----------------------
        sucursal_retiro -- Integer: Código de "Sucursal Andreani" donde el
                                    envío permanecerá en Custodia. Obligatorio
                                    para los Servicios de Retiro en Sucursal
                                    (valor "sucursal" de la consulta de
                                    sucursales)
        provincia -- String
        localidad -- String
        codigo_postal -- String: Codigo postal del destino
        calle -- String
        numero -- String
        departamento -- String
        piso -- String
        nombre_apellido -- String
        tipo_documento -- String
        numero_documento -- String
        email -- String
        numero_celular -- String
        numero_telefono -- String
        email -- String
        nombre_apellido_alternativo -- String
        numero_transaccion -- String: ID de identificación de envío del Cliente
        detalle_productos_entrega -- String
        detalle_productos_retiro -- String
        peso -- Float: Expresado en Gramos (gr.)
        volumen -- Float: Expresado en Centímetros Cúbicos (cc3.) (No es
                          obligatorio si se usan categorías de peso).
                          Considerar el volumen del envoltorio/Embalaje.
        valor_declarado -- Float: Obligatorio para los Servicios que incluye
                                 seguro en caso de siniestro
        valor_cobrar -- Float: Obligatorio para los Servicio que incluyen
                               Gestión Cobranza (pago contrareembolso)
        sucursal_cliente -- String: Nombre que identifica la sucursal/depósito
                                    del Cliente. Obligatorio para los Servicios
                                    de Retiro en Sucursal Andreani más próxima
                                    a la sucursal/depósito de Cliente
        categoria_distancia -- Integer: Código de categoría para la cotización.
                                        Obligatorio cuando la tarifas del
                                        servicio se cotizan por Categorías de
                                        Distancia
        categoria_facturacion -- Integer: Uso interno
        categoria_peso -- Integer: Código de categoría para la cotización.
                                   Obligatorio cuando la tarifas del servicio
                                   se cotizan por Categorías de Peso. (por ej.
                                   1.- Zapatos, 2.-Indumentaria)
        tarifa -- Decimal: Valor de cotización del envío. Sólo se setea
                           si se consume el servicio web de Cotización.
                           Este valor es de referencia, ya que el sistema
                           recalculará la tarifa junto con el alta.
        '''
        # configuro parametros de la peticion
        parametros = {
            'SucursalRetiro': kwargs.get('sucursal_retiro'),
            'Provincia': kwargs.get('provincia'),
            'Localidad': kwargs.get('localidad'),
            'CodigoPostalDestino': kwargs.get('codigo_postal'),
            'Calle': kwargs.get('calle'),
            'Numero': kwargs.get('numero'),
            'Departamento': kwargs.get('departamento'),
            'Piso': kwargs.get('piso'),
            'NombreApellido': kwargs.get('nombre_apellido'),
            'TipoDocumento': kwargs.get('tipo_documento'),
            'NumeroDocumento': kwargs.get('numero_documento'),
            'Email': kwargs.get('email'),
            'NumeroCelular': kwargs.get('numero_celular'),
            'NumeroTelefono': kwargs.get('numero_telefono'),
            'NombreApellidoAlternativo': kwargs.get(
                'nombre_apellido_alternativo'),
            'NumeroTransaccion': kwargs.get('numero_transaccion'),
            'DetalleProductosEntrega': kwargs.get('detalle_productos_entrega'),
            'DetalleProductosRetiro': kwargs.get('detalle_productos_retiro'),
            'Peso': kwargs.get('peso'),
            'Volumen': kwargs.get('volumen'),
            'ValorDeclarado': kwargs.get('valor_declarado'),
            'ValorACobrar': kwargs.get('valor_cobrar'),
            'Contrato': self.contrato,
            'SucursalCliente': kwargs.get('sucursal_cliente'),
            'CategoriaDistancia': kwargs.get('categoria_distancia'),
            'CategoriaFacturacion': kwargs.get('categoria_facturacion'),
            'CategoriaPeso': kwargs.get('categoria_peso'),
            'Tarifa': kwargs.get('tarifa'),
            'NumeroRecibo': kwargs.get('numero_recibo'),
        }
        # obtengo resultado
        response = self.__soap("confirmar_compra_datos_impresion",
                               compra=parametros)
        return self.__to_dict(response) if response else None

    def consultas_codigo_postal(self):
        '''
        Permite consultar Códigos Postales, Localidades, Provincias y Países.
        '''
        pass

    def consulta_trazabilidad(self):
        '''
        Permite consultar la trazabilidad de un envío.
        '''
        pass

    def consulta_ultimo_estado_distribucion(self):
        '''
        Devuelve el último estado de la Distribución de un envío, o
        una lista de envíos.
        '''
        pass

    def imprimir_constancias(self):
        '''
        Devuelve una URL que referencia al PDF correspondiente a
        la constancia de entrega de un envío determinado.
        Sólo aplica a envíos que están pendientes de impresión.
        '''
        pass

    def anular_envio(self):
        '''
        Anula envíos que todavía no hayan ingresado al circuito operativo
        '''
        pass

    def consultar_datos_impresion(self):
        '''
        Este servicio permite consultar los datos de impresión de una pieza
        dada.
        '''
        pass

    def reporte_envios_pendientes_impresion(self):
        '''
        Devuelve una lista de envíos que fueron dados a través del servicio
        "Confirmación de compra".

        Sirve para permitir su impresión mediante el servicio de "Imprimir
        constancias".
        '''
        pass

    def reporte_envios_pendientes_ingreso(self):
        '''
        Devuelve un listado de envíos que ya se imprimieron pero
        que todavía no entraron en el circuito operativo de Andreani.
        '''
        pass

    def generar_remito_imposicion(self):
        '''
        El remito de imposición es el comprobante tanto de la
        entrega de mercadería en sucursal por parte del vendedor
        como de el retiro en depósito realizado por Andreani.
        '''
        pass

    def __to_dict(self, obj):
        '''
        Convierte un objeto en diccionario.
        '''
        _dict = {}
        # itero sobre los atributos del objeto
        for attr in dir(obj):
            # si no es un atributo de python y no es una funcion
            if not attr.startswith('__') and not callable(getattr(obj, attr)):
                # agrego el atributo al diccionario
                _dict[self.__pythonize(attr)] = getattr(obj, attr)
        return _dict

    def __pythonize(self, attr):
        '''
        Pythoniza el nombre de un atributo de formato CamelCase a under_score.
        '''
        result = [attr[0].lower()]
        for char in attr[1:]:
            if char in string.ascii_uppercase:
                result.append("_")
            result.append(char.lower())
        return ''.join(result)

    def __get_wsdl(self, peticion):
        '''
        Obtiene la URL del WSDL y el nombre del metodo para la peticion
        dada. Tiene en cuenta el ambiente en el que se ejecuta.
        '''
        if self.DEBUG:
            return self._URL['Staging'][peticion]


class CodigoPostalInvalido(ValueError):
    pass


class APIError(Exception):
    pass
