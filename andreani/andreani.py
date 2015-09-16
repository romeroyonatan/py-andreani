'''
Implementa los servicios ofrecidos por el webservice de andreani.
'''
import logging

import suds
from suds.client import Client
from suds.wsse import UsernameToken, Security

# modifico namespace del envoltorio soap
from suds.bindings import binding
binding.envns=('SOAP-ENV', 'http://www.w3.org/2003/05/soap-envelope')

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
        content_type = ('application/soap+xml;charset=UTF-8;action=%s' %
                        soap.service.ConsultarSucursales.method.soap.action)
        soap.set_options(headers={'Content-Type': content_type})
        # configuro parametros de la consulta
        if codigo_postal or localidad or provincia:
            consulta = {'CodigoPostal': codigo_postal,
                        'Localidad': localidad,
                        'Provincia': provincia}
        else:
            consulta = {'CodigoPostal': suds.null()}
        # realizo la consulta y obtengo el resultado
        result = soap.service.ConsultarSucursales(consulta=consulta)
        return result

    def cotizar_envio(self, sucursal_retiro, cp_destino, peso, volumen):
        '''
        Permite cotizar en línea el costo de un envío.

        args
        --------
        sucursal_retiro -- integer: Código de "Sucursal Andreani" donde el envío
                                   permanecerá en Custodia. Obligatorio para los
                                   Servicios de Retiro en Sucursal
        cp_detino -- string: Obligatorio para los Servicios de Envío a Domicilio
        peso -- float: Expresado en gramos
        volumen -- float: Expresados en centimetros cúbicos
        '''
        pass
        # url = "https://www.e-andreani.com/CasaStaging/eCommerce/CotizacionEnvio.svc?wsdl"
        # client = self.__soap(url)
        # logging.debug(soap)
        # result = soap.service.CotizarEnvio(CPDestino=cp_destino,
                                             # Cliente=self.cliente,
                                             # Contrato=self.contrato,
                                             # Peso=peso,
                                             # SucursalRetiro=sucursal_retiro,
                                             # Volumen=volumen)
        # logging.debug(result)

    def confirmar_compra(self):
        '''
        Genera un envío en Andreani.

        Asigna un identificador con el cual se va a hacer el seguimiento.
        Luego se debe llamar al WS de Imprimir Constancia para finalizar el
        proceso de Alta del envío.
        '''
        pass

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


