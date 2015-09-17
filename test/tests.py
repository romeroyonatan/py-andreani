import logging

from unittest import TestCase
from andreani.andreani import Andreani, CodigoPostalInvalido, AndreaniError

# credenciales de prueba
TEST_USER = "eCommerce_Integra"
TEST_PASSWD = "passw0rd"
# cliente de prueba
CLIENTE = "ANDCORREO"
# Contrato entrega en domicilio urgente
CONTRATO_URGENTE = "AND00URG"
# Contrato entrega en sucursal andreani
CONTRATO_SUCURSAL = "AND00SUC"
# Contrato entrega en domicilio estandar
CONTRATO_ESTANDAR = "AND00EST"
# Contrato gestion de cambio
CONTRATO_CAMBIO = "AND00CMB"

logging.basicConfig(filename='testing.log', filemode='w', level=logging.DEBUG)


class AndreaniTests(TestCase):

    def test_consultar_sucursales(self):
        '''
        Prueba servicios de consultar sucursales habilitadas para el retiro de
        paquetes de e-commerce.
        '''
        andreani = Andreani(TEST_USER, TEST_PASSWD, CLIENTE, CONTRATO_SUCURSAL)
        # consulta sin filtros
        sucursales = andreani.consulta_sucursales()
        self.assertTrue(sucursales)
        # filtro codigo postal
        sucursales = andreani.consulta_sucursales(codigo_postal=1048)
        self.assertTrue(sucursales)
        # filtro provincia
        sucursales = andreani.consulta_sucursales(provincia="santa fe")
        self.assertTrue(sucursales)
        # filtro localidad
        sucursales = andreani.consulta_sucursales(localidad="rosario")
        self.assertTrue(sucursales)
        # filtros combinados
        sucursales = andreani.consulta_sucursales(codigo_postal=1048,
                                                  localidad="c.a.b.a.")
        self.assertTrue(sucursales)
        sucursales = andreani.consulta_sucursales(provincia="santa fe",
                                                  localidad="venado tuerto")
        self.assertTrue(sucursales)
        # todos los filtros
        sucursales = andreani.consulta_sucursales(provincia="buenos aires",
                                                  localidad="san justo",
                                                  codigo_postal=1754)
        self.assertTrue(sucursales)
        # sin resultados
        sucursales = andreani.consulta_sucursales(provincia="cordoba",
                                                  localidad="san justo")
        self.assertFalse(sucursales)
        # codigo postal invalido
        sucursales = andreani.consulta_sucursales(codigo_postal="1")
        self.assertFalse(sucursales)

    def test_cotizar_envio(self):
        '''
        Prueba servicios de cotizar envios.
        '''
        # cotizacion envio a domicilio
        andreani = Andreani(TEST_USER, TEST_PASSWD, CLIENTE, CONTRATO_ESTANDAR)
        cotizacion =  andreani.cotizar_envio(cp_destino="9410", # ushuaia
                                             peso="1",
                                             volumen="1")
        self.assertTrue(cotizacion)
        self.assertTrue(cotizacion['tarifa'])

        # cotizacion envio a sucursal
        # XXX: webservice falla si no envio cp_destino
        andreani = Andreani(TEST_USER, TEST_PASSWD, CLIENTE, CONTRATO_SUCURSAL)
        cotizacion =  andreani.cotizar_envio(sucursal_retiro="20",
                                             cp_destino="1754", # san justo
                                             peso="1000",
                                             volumen="1000")
        self.assertTrue(cotizacion)
        self.assertTrue(cotizacion['tarifa'])

        # codigo postal invalido
        with self.assertRaises(CodigoPostalInvalido):
            cotizacion =  andreani.cotizar_envio(cp_destino="1",
                                                 peso="1000",
                                                 volumen="1000")
        # peso o volumen menor que cero
        with self.assertRaises(AndreaniError):
            cotizacion =  andreani.cotizar_envio(cp_destino="1001",
                                                 peso="0",
                                                 volumen="1000")
        with self.assertRaises(AndreaniError):
            cotizacion =  andreani.cotizar_envio(cp_destino="1001",
                                                 peso="10",
                                                 volumen="0")
    def test_confirmar_compra(self):
        '''
        Prueba servicio de confirmar compra.
        '''
        parametros = { 
            'sucursal_retiro': '20',
            'provincia': 'Buenos Aires',
            'localidad': 'San Justo',
            'codigo_postal': '1754',
            'calle': 'Florencio Varela',
            'numero': '1903',
            'departamento': '',
            'piso': '',
            'nombre_apellido': 'Susana Horia',
            'tipo_documento': 'DNI',
            'numero_documento': '12345678',
            'email': 'email@example.com',
            'numero_celular': '011 15 1515 1111',
            'numero_telefono': '011 4321 1234',
            'nombre_apellido_alternativo': 'Susi',
            'numero_transaccion': '',
            'detalle_productos_entrega': 'Prueba de entrega',
            'detalle_productos_retiro': 'Prueba de envio',
            'peso': '1000',
            'volumen': '1000',
            'valor_declarado': '0.5',
            'valor_cobrar': '1.0',
            'contrato': '',
            'sucursal_cliente': '',
            'categoria_distancia': '',
            'categoria_facturacion': '',
            'categoria_peso': '',
            'tarifa': '20.0',
        }
        # confirmacion de compra con cotizacion de envio
        andreani = Andreani(TEST_USER, TEST_PASSWD, CLIENTE, CONTRATO_ESTANDAR)
        compra = andreani.confirmar_compra(**parametros)
        self.assertTrue(compra)
        print(compra)
