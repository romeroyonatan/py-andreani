import logging

import unittest
import andreani
from unittest import TestCase

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


class ConsultarSucursalesTests(TestCase):
    '''
    Prueba servicios de consultar sucursales habilitadas para el retiro de
    paquetes de e-commerce.
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER, 
                                     TEST_PASSWD, 
                                     CLIENTE,
                                     CONTRATO_SUCURSAL)
        
    def test_sin_filtros(self):
        '''
        Busca sucursales sin filtros
        '''
        sucursales = self.andreani.consulta_sucursales()
        self.assertTrue(sucursales)

    def test_filtro_codigo_postal(self):
        '''
        Busca sucursales por codigo postal.
        '''
        sucursales = self.andreani.consulta_sucursales(codigo_postal=1048)
        self.assertTrue(sucursales)

    def test_filtro_provincia(self):
        '''
        Busca sucursales por provincia.
        '''
        sucursales = self.andreani.consulta_sucursales(provincia="santa fe")
        self.assertTrue(sucursales)

    def test_filtro_localidad(self):
        '''
        Busca sucursales por localidad.
        '''
        sucursales = self.andreani.consulta_sucursales(localidad="rosario")
        self.assertTrue(sucursales)

    def test_filtros_combinados(self):
        '''
        Busca sucursales por varios filtros a la vez.
        '''
        sucursales = self.andreani.consulta_sucursales(codigo_postal=1048,
                                                  localidad="c.a.b.a.")
        self.assertTrue(sucursales)
        sucursales = self.andreani.consulta_sucursales(provincia="santa fe",
                                                  localidad="venado tuerto")
        self.assertTrue(sucursales)

    def test_todos_los_filtros(self):
        '''
        Busca sucursales por todos los filtros.
        '''
        sucursales = self.andreani.consulta_sucursales(provincia="buenos aires",
                                                  localidad="san justo",
                                                  codigo_postal=1754)
        self.assertTrue(sucursales)

    def test_sin_resultados(self):
        '''
        Busca sucursales por filtros disjuntos y espera como resultado una
        lista vacia.
        '''
        # sin resultados
        sucursales = self.andreani.consulta_sucursales(provincia="cordoba",
                                                  localidad="san justo")
        self.assertFalse(sucursales)

    def test_codigo_postal_invalido(self):
        '''
        Busca sucursales por un codigo postal inexistente
        '''
        # codigo postal invalido
        sucursales = self.andreani.consulta_sucursales(codigo_postal="1")
        self.assertFalse(sucursales)

class CotizarEnvioTests(TestCase):
    '''
    Prueba servicios de cotizar envios.
    '''

    def setUp(self):
        self.andreani = andreani.API(TEST_USER, 
                                     TEST_PASSWD, 
                                     CLIENTE,
                                     CONTRATO_SUCURSAL)

    def test_cotizar_envio_domicilio(self):
        '''
        Cotizacion envio a domicilio.
        '''
        api = andreani.API(TEST_USER, TEST_PASSWD, CLIENTE, CONTRATO_ESTANDAR)
        cotizacion = api.cotizar_envio(cp_destino="9410", # ushuaia
                                       peso="1",
                                       volumen="1")
        self.assertTrue(cotizacion)
        self.assertTrue(cotizacion['tarifa'])

    def test_cotizar_envio_sucursal(self):
        '''
        Cotizacion envio a sucursal.
        '''
        cotizacion = self.andreani.cotizar_envio(sucursal_retiro="20",
                                                 cp_destino="1754", # san justo
                                                 peso="1000",
                                                 volumen="1000")
        self.assertTrue(cotizacion)
        self.assertTrue(cotizacion['tarifa'])

    def test_codigo_postal_invalido(self):
        '''
        Cotizacion con un codigo postal inexistente.
        '''
        with self.assertRaises(andreani.CodigoPostalInvalido):
            cotizacion = self.andreani.cotizar_envio(cp_destino="1",
                                                     peso="1000",
                                                     volumen="1000")

    def test_volumen_menor_cero(self):
        '''
        Cotizacion de un paquete de volumen menor o igual a cero
        '''
        with self.assertRaises(ValueError):
            cotizacion = self.andreani.cotizar_envio(cp_destino="1001",
                                                      peso="10",
                                                      volumen="0")
        with self.assertRaises(ValueError):
            cotizacion = self.andreani.cotizar_envio(cp_destino="1001",
                                                     peso="10",
                                                     volumen="-1000")
    def test_peso_menor_cero(self):
        '''
        Cotizacion de un paquete de peso menor o igual a cero
        '''
        with self.assertRaises(ValueError):
            cotizacion =  self.andreani.cotizar_envio(cp_destino="1001",
                                                 peso="0",
                                                 volumen="1000")
        with self.assertRaises(ValueError):
            cotizacion =  self.andreani.cotizar_envio(cp_destino="1001",
                                                      peso="-10",
                                                      volumen="10")
class ConfirmarCompraTests(TestCase):
    '''
    Prueba servicios de confirmar compra.
    '''

    def setUp(self):
        self.andreani = andreani.API(TEST_USER, 
                                     TEST_PASSWD, 
                                     CLIENTE,
                                     CONTRATO_SUCURSAL)

    @unittest.expectedFailure
    def test_con_cotizacion_envio(self):
        '''
        Prueba servicio de confirmar compra con cotizacion de envio
        '''
        # configuro parametros de la compra
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
        # XXX: el servidor retorna "Servicio no habilitado"
        compra = self.andreani.confirmar_compra(**parametros)
        self.assertTrue(compra)
