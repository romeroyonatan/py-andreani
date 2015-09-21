import logging

import andreani
from unittest import TestCase, mock

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
        self.andreani.DEBUG = True

    def test_sin_filtros(self):
        '''
        Busca sucursales sin filtros
        '''
        self.andreani._API__soap = mock.MagicMock(return_value=[[
            type('testclass', (object,), {
                "Descripcion": "9 DE JULIO",
                "Direccion": "Bme. Mitre 1668, 6500, 9 DE JULIO, BUENOS AIRES",
                "HoradeTrabajo": None,
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "NDJ",
                "Responsable": None,
                "Resumen": "9 DE JULIO",
                "Sucursal": 71,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 2,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
            type('testclass', (object,), {
                "Descripcion": "TRIBUNALES",
                "Direccion": "MOLINEDO 1600, 1870 ,AVELLANEDA, BUENOS AIRES",
                "HoradeTrabajo": "De Lunes a Viernes de 08:30 a 17:30",
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "TRI",
                "Responsable": None,
                "Resumen": "TRIBUNALES",
                "Sucursal": 129,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 3,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
            type('testclass', (object,), {
                "Descripcion": "AZUL",
                "Direccion": "Perón 441 , 7300 , AZUL , BUENOS AIRES",
                "HoradeTrabajo": None,
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "AZU",
                "Responsable": None,
                "Resumen": "AZUL",
                "Sucursal": 34,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 2,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
        ]])
        sucursales = self.andreani.consultar_sucursales()
        self.assertTrue(sucursales)

    def test_filtro_codigo_postal(self):
        '''
        Busca sucursales por codigo postal.
        '''
        self.andreani._API__soap = mock.MagicMock(return_value=[[
            type('testclass', (object,), {
                "Descripcion": "AZUL",
                "Direccion": "Perón 441 , 7300 , AZUL , BUENOS AIRES",
                "HoradeTrabajo": None,
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "AZU",
                "Responsable": None,
                "Resumen": "AZUL",
                "Sucursal": 34,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 2,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
        ]])
        sucursales = self.andreani.consultar_sucursales(codigo_postal=7300)
        self.assertTrue(sucursales)

    def test_filtro_provincia(self):
        '''
        Busca sucursales por provincia.
        '''
        self.andreani._API__soap = mock.MagicMock(return_value=[[
            type('testclass', (object,), {
                "Descripcion": "9 DE JULIO",
                "Direccion": "Bme. Mitre 1668, 6500, 9 DE JULIO, BUENOS AIRES",
                "HoradeTrabajo": None,
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "NDJ",
                "Responsable": None,
                "Resumen": "9 DE JULIO",
                "Sucursal": 71,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 2,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
            type('testclass', (object,), {
                "Descripcion": "TRIBUNALES",
                "Direccion": "MOLINEDO 1600, 1870 ,AVELLANEDA, BUENOS AIRES",
                "HoradeTrabajo": "De Lunes a Viernes de 08:30 a 17:30",
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "TRI",
                "Responsable": None,
                "Resumen": "TRIBUNALES",
                "Sucursal": 129,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 3,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
            type('testclass', (object,), {
                "Descripcion": "AZUL",
                "Direccion": "Perón 441 , 7300 , AZUL , BUENOS AIRES",
                "HoradeTrabajo": None,
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "AZU",
                "Responsable": None,
                "Resumen": "AZUL",
                "Sucursal": 34,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 2,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
        ]])
        sucursales = self.andreani.consultar_sucursales(
            provincia="Buenos Aires")
        self.assertTrue(sucursales)

    def test_filtro_localidad(self):
        '''
        Busca sucursales por localidad.
        '''
        self.andreani._API__soap = mock.MagicMock(return_value=[[
            type('testclass', (object,), {
                "Descripcion": "AZUL",
                "Direccion": "Perón 441 , 7300 , AZUL , BUENOS AIRES",
                "HoradeTrabajo": None,
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "AZU",
                "Responsable": None,
                "Resumen": "AZUL",
                "Sucursal": 34,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 2,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
        ]])
        sucursales = self.andreani.consultar_sucursales(localidad="azul")
        self.assertTrue(sucursales)

    def test_filtros_combinados(self):
        '''
        Busca sucursales por varios filtros a la vez.
        '''
        self.andreani._API__soap = mock.MagicMock(return_value=[[
            type('testclass', (object,), {
                "Descripcion": "AZUL",
                "Direccion": "Perón 441 , 7300 , AZUL , BUENOS AIRES",
                "HoradeTrabajo": None,
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "AZU",
                "Responsable": None,
                "Resumen": "AZUL",
                "Sucursal": 34,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 2,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
        ]])
        sucursales = self.andreani.consultar_sucursales(
            codigo_postal=7300,
            localidad="azul")
        self.assertTrue(sucursales)
        sucursales = self.andreani.consultar_sucursales(
            provincia="Buenos Aires",
            localidad="Azul")
        self.assertTrue(sucursales)

    def test_todos_los_filtros(self):
        '''
        Busca sucursales por todos los filtros.
        '''
        self.andreani._API__soap = mock.MagicMock(return_value=[[
            type('testclass', (object,), {
                "Descripcion": "TRIBUNALES",
                "Direccion": "MOLINEDO 1600, 1870 ,AVELLANEDA, BUENOS AIRES",
                "HoradeTrabajo": "De Lunes a Viernes de 08:30 a 17:30",
                "Latitud": None,
                "Longitud": None,
                "Mail": None,
                "Numero": "TRI",
                "Responsable": None,
                "Resumen": "TRIBUNALES",
                "Sucursal": 129,
                "Telefono1": "0810-122-1111",
                "Telefono2": "0800-122-1112",
                "Telefono3": None,
                "TipoSucursal": 3,
                "TipoTelefono1": None,
                "TipoTelefono2": None,
                "TipoTelefono3": None
            })(),
        ]])
        sucursales = self.andreani.consultar_sucursales(
            codigo_postal=1870,
            provincia="buenos aires",
            localidad="avellaneda")
        self.assertTrue(sucursales)

    def test_sin_resultados(self):
        '''
        Busca sucursales por filtros disjuntos y espera como resultado una
        lista vacia.
        '''
        # sin resultados
        self.andreani._API__soap = mock.MagicMock(return_value=[[]])
        sucursales = self.andreani.consultar_sucursales(
            provincia="cordoba",
            localidad="san justo")
        self.assertFalse(sucursales)

    def test_codigo_postal_invalido(self):
        '''
        Busca sucursales por un codigo postal inexistente
        '''
        self.andreani._API__soap = mock.MagicMock(return_value=[[]])
        # codigo postal invalido
        sucursales = self.andreani.consultar_sucursales(codigo_postal="1")
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
        self.andreani.DEBUG = True

    def test_cotizar_envio_domicilio(self):
        '''
        Cotizacion envio a domicilio.
        '''
        api = andreani.API(TEST_USER, TEST_PASSWD, CLIENTE, CONTRATO_ESTANDAR)
        api._API__soap = mock.MagicMock(
            return_value=type('testclass', (object,), {
                "CategoriaDistancia": "INTERIOR 1",
                "CategoriaDistanciaId": "2",
                "CategoriaPeso": "1",
                "CategoriaPesoId": "1",
                "PesoAforado": 1.0,
                "Tarifa": 55.9,
            })())
        api.DEBUG = True
        cotizacion = api.cotizar_envio(cp_destino="9410",  # ushuaia
                                       peso="1",
                                       volumen="1")
        self.assertTrue(cotizacion)
        self.assertTrue(cotizacion['tarifa'])

    def test_cotizar_envio_sucursal(self):
        '''
        Cotizacion envio a sucursal.
        '''
        self.andreani._API__soap = mock.MagicMock(
            return_value=type('testclass', (object,), {
                "CategoriaDistancia": "INTERIOR 1",
                "CategoriaDistanciaId": "2",
                "CategoriaPeso": "1",
                "CategoriaPesoId": "1",
                "PesoAforado": 1.0,
                "Tarifa": 55.9,
            })())
        cotizacion = self.andreani.cotizar_envio(sucursal_retiro="20",
                                                 cp_destino="1754",
                                                 peso="1000",
                                                 volumen="1000")
        self.assertTrue(cotizacion)
        self.assertTrue(cotizacion['tarifa'])

    def test_codigo_postal_invalido(self):
        '''
        Cotizacion con un codigo postal inexistente.
        '''
        self.andreani._API__soap = mock.MagicMock(
            side_effect=andreani.CodigoPostalInvalido())
        with self.assertRaises(andreani.CodigoPostalInvalido):
            self.andreani.cotizar_envio(cp_destino="1",
                                        peso="1000",
                                        volumen="1000")

    def test_volumen_menor_cero(self):
        '''
        Cotizacion de un paquete de volumen menor o igual a cero
        '''
        with self.assertRaises(ValueError):
            self.andreani.cotizar_envio(cp_destino="1001",
                                        peso="10",
                                        volumen="0")
        with self.assertRaises(ValueError):
            self.andreani.cotizar_envio(cp_destino="1001",
                                        peso="10",
                                        volumen="-1000")

    def test_peso_menor_cero(self):
        '''
        Cotizacion de un paquete de peso menor o igual a cero
        '''
        with self.assertRaises(ValueError):
            self.andreani.cotizar_envio(cp_destino="1001",
                                        peso="0",
                                        volumen="1000")
        with self.assertRaises(ValueError):
            self.andreani.cotizar_envio(cp_destino="1001",
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
        self.andreani.DEBUG = True

        # configuro parametros de la compra
        self.parametros = {
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

    def test_con_cotizacion_envio(self):
        '''
        Prueba servicio de confirmar compra con cotizacion de envio
        '''
        self.andreani._API__soap = mock.MagicMock(
            return_value=type('testclass', (object,), {
                "NumeroAndreani": "*00000000252903",
                "Recibo": None
            })())
        compra = self.andreani.confirmar_compra(**self.parametros)
        self.assertTrue(compra)

    def test_con_datos_impresion(self):
        '''
        Prueba servicio de confirmar compra con cotizacion de envio.
        '''
        self.andreani._API__soap = mock.MagicMock(
            return_value=type('testclass', (object,), {
                "NumeroAndreani": "*00000000252903",
                "Recibo": "RETA01PSD00000001"
            })())
        self.parametros['numero_recibo'] = "1"
        compra = self.andreani.confirmar_compra_datos_impresion(
            **self.parametros)
        self.assertTrue(compra)
