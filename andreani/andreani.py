'''
Implementa los servicios ofrecidos por el webservice de andreani.
'''

class Andreani(object):
'''
Implementa los servicios ofrecidos por el webservice de andreani.
'''

    def consulta_sucursales(self):
        '''
        Devuelve una lista de sucursales Andreani habilitadas para la entrega 
        por mostrador.'''
        pass
    
    def cotizar_envios(self):
        '''
        Permite cotizar en línea el costo de un envío.
        '''
        pass
    
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
