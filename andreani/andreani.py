'''
Implementa los servicios ofrecidos por el webservice de andreani.
'''
import logging
import string
from gettext import gettext as _

import suds
from suds.client import Client
from suds.wsse import UsernameToken, Security

# modifico namespace del envoltorio soap
from suds.bindings import binding
binding.envns = ('SOAP-ENV', 'http://www.w3.org/2003/05/soap-envelope')


class Andreani(object):

    '''
    Implementa los servicios ofrecidos por el webservice de andreani.
    '''

    def __init__(self, username, password, cliente, contrato):
        '''
        Inicializa datos del objeto
        '''
        # guardo token generado como atributo del objeto
        token = UsernameToken(username, password)
        self.security = Security()
        self.security.tokens.append(token)
        # numero de cliente
        self.cliente = cliente
        # numero de servicio andreani
        self.contrato = contrato

    def __soap(self, url):
        '''
        Obtiene un cliente SOAP para utilizar.
        '''
        client = Client(url)
        client.set_options(wsse=self.security)
        return client

    def consulta_sucursales(self, codigo_postal=None,
                            localidad=None,
                            provincia=None):
        '''
        Devuelve una lista de sucursales Andreani habilitadas para la entrega
        por mostrador.
        '''
        # configuro url del wsdl
        url = ("https://www.e-andreani.com/CasaStaging/eCommerce/" +
               "ConsultaSucursales.svc?wsdl")
        soap = self.__soap(url)
        # configuro content-type de la peticion
        # XXX: es obligatorio para el servidor que el parametro action este
        # dentro de la cabecera 'Content-Type'
        content_type = ('application/soap+xml;charset=UTF-8;action=%s' %
                        soap.service.ConsultarSucursales.method.soap.action)
        soap.set_options(headers={'Content-Type': content_type})
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
        result = soap.service.ConsultarSucursales(consulta=consulta)
        # devuelvo lista de sucursales
        try:
            if result:
                return [self.__to_dict(sucursal) for sucursal in result[0]]
            else:
                return []
        except suds.WebFault as e:
            raise AndreaniError(e.fault.Reason.Text) from e

    def cotizar_envio(self, peso, volumen, cp_destino, sucursal_retiro=None):
        '''
        Permite cotizar en línea el costo de un envío.

        args
        --------
        sucursal_retiro -- integer: Código de "Sucursal Andreani" donde el envío
                                   permanecerá en Custodia. Obligatorio para los
                                   Servicios de Retiro en Sucursal
        cp_destino -- string: Obligatorio para los Servicios de Envío a 
                              Domicilio
        peso -- float: Expresado en gramos
        volumen -- float: Expresados en centimetros cúbicos
        '''
        self.validar_cotizacion(peso, volumen, cp_destino, sucursal_retiro)
        # configuro url del wsdl
        url = ("https://www.e-andreani.com/CasaStaging/eCommerce/" +
               "CotizacionEnvio.svc?wsdl")
        soap = self.__soap(url)
        # configuro content-type de la peticion
        # XXX: es obligatorio para el servidor que el parametro action este
        # dentro de la cabecera 'Content-Type'
        content_type = ('application/soap+xml;charset=UTF-8;action=%s' %
                        soap.service.CotizarEnvio.method.soap.action)
        soap.set_options(headers={'Content-Type': content_type})
        # configuro parametros de la peticion
        cotizacion_envio = {'CPDestino': cp_destino,
                            'Cliente': self.cliente,
                            'Contrato': self.contrato,
                            'Peso': peso,
                            'SucursalRetiro': sucursal_retiro,
                            'Volumen': volumen,
                           }
        # obtengo resultado
        try:
            result = soap.service.CotizarEnvio(cotizacionEnvio=cotizacion_envio)
            if result:
                return self.__to_dict(result)
            else:
                return None
        # tratamiento de excepcion
        except suds.WebFault as e:
            text = e.fault.Reason.Text
            if text == "Codigo postal es invalido":
                raise CodigoPostalInvalido from e
            raise AndreaniError(text) from e
        
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
        # configuro url del wsdl
        url = ("https://www.e-andreani.com/CasaStaging/eCommerce/" +
               "ImposicionRemota.svc?wsdl")
        soap = self.__soap(url)
        # configuro content-type de la peticion
        # XXX: es obligatorio para el servidor que el parametro action este
        # dentro de la cabecera 'Content-Type'
        content_type = ('application/soap+xml;charset=UTF-8;action=%s' %
                        soap.service.ConfirmarCompra.method.soap.action)
        soap.set_options(headers={'Content-Type': content_type})
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
        try:
            result = soap.service.ConfirmarCompra(compra=parametros)
            return self.__to_dict(result) if result else None
        # tratamiento de excepcion
        except suds.WebFault as e:
            raise AndreaniError(e.fault.Reason.Text) from e

    def confirmar_compra_datos_impresion(self):
        '''
        Genera un envío y devuelve todos los datos necesarios para
        que el cliente imprima la etiqueta del bulto.

        A diferencia del Confirmar compra el pedido finaliza el proceso de Alta,
        El uso de este Web Services es recomendado para cliente que
        tienen altas intensivas y un proceso de preparación que
        necesita agilidad
        '''
        pass

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

    def validar_cotizacion(self, peso, volumen, codigo_postal, sucursal_retiro):
        '''
        Valida parametros para cotizar un envio.
        '''
        if float(peso) <= 0:
            raise AndreaniError(_("Peso debe ser mayor a cero"))
        if float(volumen) <= 0:
            raise AndreaniError(_("Volumen debe ser mayor a cero"))

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

class CodigoPostalInvalido(ValueError):
    pass
class AndreaniError(Exception):
    pass
