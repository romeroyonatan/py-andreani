import logging

import unittest
import andreani
import suds
import suds.client
from suds.sudsobject import Factory
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

# Activa mocks para pruebas. Si los mocks están desactivados, las peticiones
# irán realmente a los servidores de Andreani. Caso contrario, se simularán
# las respuestas del servidor
MOCK = True

logging.basicConfig(filename='testing.log', filemode='w', level=logging.DEBUG)


class ConsultarSucursalesTests(TestCase):
    '''
    Prueba servicios de consultar sucursales habilitadas para el retiro de
    paquetes de e-commerce.
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_sin_filtros(self):
        '''
        Busca sucursales sin filtros
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(return_value=[[
                Factory.object(dict={
                    "Descripcion": "9 DE JULIO",
                    "Direccion": "Bme.Mitre 1668,6500,9 DE JULIO,BUENOS AIRES",
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
                }),
                Factory.object(dict={
                    "Descripcion": "TRIBUNALES",
                    "Direccion": "MOLINEDO 1600,1870,AVELLANEDA,BUENOS AIRES",
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
                }),
                Factory.object(dict={
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
                }),
            ]])
        sucursales = self.andreani.consultar_sucursales()
        self.assertTrue(sucursales)

    def test_filtro_codigo_postal(self):
        '''
        Busca sucursales por codigo postal.
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(return_value=[[
                Factory.object(dict={
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
                }),
            ]])
        sucursales = self.andreani.consultar_sucursales(codigo_postal=7300)
        self.assertTrue(sucursales)

    def test_filtro_provincia(self):
        '''
        Busca sucursales por provincia.
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(return_value=[[
                Factory.object(dict={
                    "Descripcion": "9 DE JULIO",
                    "Direccion": "Bme.Mitre1668,6500,9 DE JULIO,BUENOS AIRES",
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
                }),
                Factory.object(dict={
                    "Descripcion": "TRIBUNALES",
                    "Direccion": "MOLINEDO 1600,1870,AVELLANEDA,BUENOS AIRES",
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
                }),
                Factory.object(dict={
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
                }),
            ]])
        sucursales = self.andreani.consultar_sucursales(
            provincia="Buenos Aires")
        self.assertTrue(sucursales)

    def test_filtro_localidad(self):
        '''
        Busca sucursales por localidad.
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(return_value=[[
                Factory.object(dict={
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
                }),
            ]])
        sucursales = self.andreani.consultar_sucursales(localidad="azul")
        self.assertTrue(sucursales)

    def test_filtros_combinados(self):
        '''
        Busca sucursales por varios filtros a la vez.
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(return_value=[[
                Factory.object(dict={
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
                }),
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
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(return_value=[[
                Factory.object(dict={
                    "Descripcion": "TRIBUNALES",
                    "Direccion": "MOLINEDO 1600,1870,AVELLANEDA,BUENOS AIRES",
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
                }),
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
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(return_value=[[]])
        sucursales = self.andreani.consultar_sucursales(
            provincia="cordoba",
            localidad="san justo")
        self.assertFalse(sucursales)

    def test_codigo_postal_invalido(self):
        '''
        Busca sucursales por un codigo postal inexistente
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(return_value=[[]])
        sucursales = self.andreani.consultar_sucursales(codigo_postal="1")
        self.assertFalse(sucursales)


class CotizarEnvioTests(TestCase):
    '''
    Prueba servicios de cotizar envios.
    '''

    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_cotizar_envio_domicilio(self):
        '''
        Cotizacion envio a domicilio.
        '''
        api = andreani.API(TEST_USER, TEST_PASSWD, CLIENTE)
        api.DEBUG = True
        if MOCK:
            api._API__soap = mock.MagicMock(
                return_value=Factory.object(dict={
                    "CategoriaDistancia": "INTERIOR 1",
                    "CategoriaDistanciaId": "2",
                    "CategoriaPeso": "1",
                    "CategoriaPesoId": "1",
                    "PesoAforado": 1.0,
                    "Tarifa": 55.9,
                }))
        cotizacion = api.cotizar_envio(cp_destino="9410",  # ushuaia
                                       peso="1",
                                       contrato=CONTRATO_ESTANDAR,
                                       volumen="1")
        self.assertTrue(cotizacion)
        self.assertTrue(cotizacion['tarifa'])

    def test_cotizar_envio_sucursal(self):
        '''
        Cotizacion envio a sucursal.
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(dict={
                    "CategoriaDistancia": "INTERIOR 1",
                    "CategoriaDistanciaId": "2",
                    "CategoriaPeso": "1",
                    "CategoriaPesoId": "1",
                    "PesoAforado": 1.0,
                    "Tarifa": 55.9,
                }))
        cotizacion = self.andreani.cotizar_envio(sucursal_retiro="20",
                                                 cp_destino="1754",
                                                 peso="1000",
                                                 contrato=CONTRATO_ESTANDAR,
                                                 volumen="1000")
        self.assertTrue(cotizacion)
        self.assertTrue(cotizacion['tarifa'])

    @unittest.skipIf(not MOCK, "Mock desactivados")
    @mock.patch.object(suds.client.Client, '__new__')
    def test_codigo_postal_invalido(self, fake_client):
        '''
        Cotizacion con un codigo postal inexistente.
        '''
        # creo un cliente suds falso
        client = suds.client.Client('fake_url')
        # el cliente falso retornará codigo postal invalido
        client.service.CotizarEnvio.side_effect = suds.WebFault(
            type("testclass", (object,), {
                "Reason": type("testclass", (object,), {
                               "Text": "Codigo postal es invalido"}),
            }), None)
        fake_client.return_value = client
        # pruebo que lanze excepcion
        with self.assertRaises(andreani.CodigoPostalInvalido):
            self.andreani.cotizar_envio(cp_destino="1",
                                        peso="1000",
                                        contrato=CONTRATO_ESTANDAR,
                                        volumen="1000")

    @unittest.skipIf(not MOCK, "Mock desactivados")
    @mock.patch.object(suds.client.Client, '__new__')
    def test_api_error(self, fake_client):
        '''
        Prueba como reacciona modulo ante una excepcion en el webservice
        '''
        # creo un cliente suds falso
        client = suds.client.Client('fake_url')
        # el cliente falso retornará codigo postal invalido
        client.service.CotizarEnvio.side_effect = suds.WebFault(
            type("testclass", (object,), {
                "Reason": type("testclass", (object,), {
                               "Text": "Error 500"}),
            }), None)
        fake_client.return_value = client
        # pruebo que lanze excepcion
        with self.assertRaises(andreani.APIError):
            self.andreani.cotizar_envio(cp_destino="1",
                                        peso="1000",
                                        volumen="1000",
                                        contrato=CONTRATO_ESTANDAR)

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
                                     CLIENTE)
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
            'contrato': CONTRATO_ESTANDAR,
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
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(dict={
                    "NumeroAndreani": "*00000000252903",
                    "Recibo": None
                }))
        compra = self.andreani.confirmar_compra(**self.parametros)
        self.assertTrue(compra)

    def test_con_datos_impresion(self):
        '''
        Prueba servicio de confirmar compra con cotizacion de envio.
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(dict={
                    "NumeroAndreani": "*00000000252903",
                    "Recibo": "RETA01PSD00000001"
                }))
        self.parametros['numero_recibo'] = "1"
        compra = self.andreani.confirmar_compra_datos_impresion(
            **self.parametros)
        self.assertTrue(compra)


class ConsultarTrazabilidadTests(TestCase):
    '''
    Set de pruebas de consulta de trazabilidad de un envio.
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_consultar_trazabilidad(self):
        '''
        Consulta la trazabilidad de un paquete no enviado.
        '''
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(dict={
                    "NumeroEnvio": "103",
                    "Envios": [
                        Factory.object(dict={
                            "NombreEnvio": "Constancia de Envío",
                            "NroAndreani": "*00000000249801",
                            "FechaAlta": "2015-07-22 10:10:50-03:00",
                            "Eventos": [
                                Factory.object(dict={
                                    "Fecha": "2015-07-22 10:10:50-03:00",
                                    "IdEstado": 30,
                                    "Estado": "Envío no ingresado",
                                    "IdMotivo": -1,
                                    "Motivo": None,
                                    "Sucursal": "Sucursal Genérica"})
                            ],
                        }),
                    ],
                }))
            envio = "*00000000249801"
        else:
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
                'contrato': CONTRATO_ESTANDAR,
                'sucursal_cliente': '',
                'categoria_distancia': '',
                'categoria_facturacion': '',
                'categoria_peso': '',
                'tarifa': '20.0',
            }
            response = self.andreani.confirmar_compra(**parametros)
            envio = response["numero_andreani"]

        trazabilidad = self.andreani.consultar_trazabilidad(
            numero_pieza=envio)
        self.assertTrue(trazabilidad)


class CodigoPostalTests(TestCase):
    '''
    Set de pruebas de consulta de codigo postal
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_cp(self):
        if MOCK:
            # configuro lo que devolvera el mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(
                    dict={"ConsultarCodigoPostalOk": [
                        Factory.object(dict={"Response": [
                            Factory.object(dict={'Result': [dict(
                                ResultCode=10,
                                ResultDescription="Operación exitosa.-"
                            )]}),
                            Factory.object(dict={'CodigoPostal': [dict(
                                CodigoPostal=1001,
                                Nombre="CAPITAL FEDERAL",
                                Observaciones=None,
                                CodigoProvincia="C",
                                NombreProvincia="Capital Federal",
                            )]}),
                        ]}),
                    ]}
                ))
        # realizo peticion
        cp = self.andreani.consultar_codigo_postal(1001)
        self.assertTrue(cp)


class PendientesImpresionTests(TestCase):
    '''
    Set de pruebas de consulta de reportes de envios pendientes de impresion
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_reporte(self):
        '''
        Pruebo que obtenga los envios pendientes de impresion del cliente de
        pruebas.
        '''
        if MOCK:
            # configuro lo que devolvera el mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(
                    dict={"ResultadoReporteEnviosPendientesImpresion": [
                        Factory.object(dict=dict(
                            Calle="Florencio Varela",
                            Departamento=None,
                            DetalleProductosaEntregar="Prueba de entrega",
                            Localidad="11 DE SEPTIEMBRE",
                            NombreyApellido="Susana Horia",
                            Numero="1903",
                            NumeroAndreani="*00000010310340",
                            Piso=None,
                            Provincia="BUENOS AIRES",
                        )),
                        Factory.object(dict=dict(
                            Calle="Florencio Varela",
                            Departamento=None,
                            DetalleProductosaEntregar="Prueba de entrega",
                            Localidad="11 DE SEPTIEMBRE",
                            NombreyApellido="Susana Horia",
                            Numero="1903",
                            NumeroAndreani="*00000010310350",
                            Piso=None,
                            Provincia="BUENOS AIRES",
                        )),
                        Factory.object(dict=dict(
                            Calle="Florencio Varela",
                            Departamento=None,
                            DetalleProductosaEntregar="Prueba de entrega",
                            Localidad="11 DE SEPTIEMBRE",
                            NombreyApellido="Susana Horia",
                            Numero="1903",
                            NumeroAndreani="*00000010310370",
                            Piso=None,
                            Provincia="BUENOS AIRES",
                        ))]}))
        # consulto envios pendientes de impresion
        reporte = self.andreani.reporte_envios_pendientes_impresion()
        self.assertTrue(reporte)
        self.assertTrue(reporte[0]["calle"])


class ImprimirConstanciaTests(TestCase):
    '''
    Set de pruebas de impresion de constancias
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_pendiente_impresion(self):
        '''
        Pruebo que obtenga los links PDF para imprimir en caso de envios
        pendientes de impresion.
        '''
        if MOCK:
            # configuro respuesta del mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(
                    dict={"ResultadoImprimirConstancia": [
                        Factory.object(dict={
                            "PdfLinkFile": "http://fake_url.com/pdf",
                        })
                    ]}))
        pdf = self.andreani.imprimir_constancia("*00000010310370")
        self.assertTrue(pdf)
        self.assertIn("http", pdf)

    @unittest.skipIf(not MOCK, "Mock desactivados")
    @mock.patch.object(suds.client.Client, '__new__')
    def test_envio_inexistente(self, fake_client):
        '''
        Pruebo que obtenga los links PDF para imprimir en caso de numero de
        envio inexistente.
        '''
        # creo un cliente suds falso
        client = suds.client.Client('fake_url')
        # el cliente falso retornará error
        client.service.ImprimirConstancia.side_effect = suds.WebFault(
            type("testclass", (object,), {
                "Reason": type("testclass", (object,), {
                               "Text": """No se pudo generar la constancia,
                               por favor reintente en unos minutos """}),
            })(), None)
        fake_client.return_value = client
        with self.assertRaises(andreani.APIError):
            self.andreani.imprimir_constancia("*10000000249801")


class PendientesIngresoTests(TestCase):
    '''
    Set de pruebas de consulta de reportes de envios pendientes de ingreso al
    circuito Andreani
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_reporte(self):
        '''
        Pruebo que obtenga los envios pendientes de ingreso del cliente de
        pruebas.
        '''
        if MOCK:
            # configuro lo que devolvera el mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(
                    dict={"ResultadoReporteEnviosPendientesIngreso": [
                        Factory.object(dict=dict(
                            Calle="Florencio Varela",
                            Departamento=None,
                            DetalleProductosaEntregar="Prueba de entrega",
                            Localidad="11 DE SEPTIEMBRE",
                            NombreyApellido="Susana Horia",
                            Numero="1903",
                            NumeroAndreani="*00000010310340",
                            Piso=None,
                            Provincia="BUENOS AIRES",
                        )),
                        Factory.object(dict=dict(
                            Calle="CAMINO JESUS MARIA",
                            Departamento=None,
                            DetalleProductosaEntregar=" ddd",
                            Localidad="ACHIRAS",
                            NombreyApellido="Bagley Argentina S.A.(Cordoba)",
                            Numero="KM 5.5",
                            NumeroAndreani="*00000000186207",
                            Piso=None,
                            Provincia="CORDOBA",
                        )),
                        Factory.object(dict=dict(
                            Calle="Florencio Varela",
                            Departamento=None,
                            DetalleProductosaEntregar="Prueba de entrega",
                            Localidad="11 DE SEPTIEMBRE",
                            NombreyApellido="Susana Horia",
                            Numero="1903",
                            NumeroAndreani="*00000010310370",
                            Piso=None,
                            Provincia="BUENOS AIRES",
                        ))]}))
        # consulto envios pendientes de impresion
        reporte = self.andreani.reporte_envios_pendientes_ingreso()
        self.assertTrue(reporte)
        self.assertGreater(len(reporte), 1)
        self.assertTrue(reporte[1]["provincia"])

    @unittest.skipIf(not MOCK, "Mock desactivados")
    def test_lista_vacia(self):
        '''
        Pruebo con una lista vacia.
        '''
        if MOCK:
            # configuro lo que devolvera el mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(
                    dict={"ResultadoReporteEnviosPendientesIngreso": []}))
        # consulto envios pendientes de impresion
        reporte = self.andreani.reporte_envios_pendientes_ingreso()
        self.assertFalse(reporte)
        self.assertEqual(len(reporte), 0)


class AnularEnvioTests(TestCase):
    '''
    Set de pruebas de anular envios
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_pendiente_ingreso(self):
        '''
        Pruebo que anule un envio pendiente de ingreso.
        '''
        if MOCK:
            # configuro respuesta del mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(dict={
                    "ResultadoAnularEnvios": [
                        Factory.object(dict={
                            "CodigoTransaccion": "1234",
                            "Destinatario": "Susana Horia",
                            "IdCliente": CLIENTE,
                            "NumeroAndreani": "*00000010310370",
                            "Productos": "Producto de prueba",
                        })]
                }))
            envio = "*00000010310370"
        else:
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
                'contrato': CONTRATO_ESTANDAR,
                'sucursal_cliente': '',
                'categoria_distancia': '',
                'categoria_facturacion': '',
                'categoria_peso': '',
                'tarifa': '20.0',
            }
            response = self.andreani.confirmar_compra(**parametros)
            envio = response["numero_andreani"]
        response = self.andreani.anular_envio(envio)
        self.assertTrue(response)

    @unittest.skipIf(not MOCK, "Mock desactivados")
    @mock.patch.object(suds.client.Client, '__new__')
    def test_envio_inexistente(self, fake_client):
        '''
        Pruebo que obtenga los links PDF para imprimir en caso de numero de
        envio inexistente.
        '''
        # creo un cliente suds falso
        client = suds.client.Client('fake_url')
        # el cliente falso retornará error
        client.service.AnularEnvios.side_effect = suds.WebFault(
            type("testclass", (object,), {
                "Reason": type("testclass", (object,), {
                               "Text": "Envio inexistente."}),
            })(), None)
        fake_client.return_value = client

        with self.assertRaises(andreani.APIError):
            self.andreani.anular_envio("*10000000249801")

    def test_envio_anulado(self,):
        '''
        Pruebo que anule un envio ya anulado.
        '''
        # configuro respuesta del mock
        if MOCK:
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(dict={"ResultadoAnularEnvios": []}))
        response = self.andreani.anular_envio("*00000010310370")
        self.assertFalse(response)


class GenerarRemitoImposicionTests(TestCase):
    '''
    Set de pruebas de generar remito de imposicion
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_pendiente_impresion(self):
        '''
        Pruebo que obtenga los links PDF para imprimir en caso de envios
        pendientes de impresion.
        '''
        if MOCK:
            # configuro respuesta del mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(
                    dict={"ResultadoGeneracionRemitodeImposicion": [
                        Factory.object(dict={
                            "Entidades": ["Andreani1234"],
                            "Pdf": "http://fake_url.com/pdf",
                            "RemitodeImposicion": "1234567890A",
                        })
                    ]}
                )
            )
            envio = "*00000010310370"
        else:
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
                'contrato': CONTRATO_ESTANDAR,
                'sucursal_cliente': '',
                'categoria_distancia': '',
                'categoria_facturacion': '',
                'categoria_peso': '',
                'tarifa': '20.0',
            }
            response = self.andreani.confirmar_compra(**parametros)
            envio = response["numero_andreani"]

        remito = self.andreani.generar_remito_imposicion(envio)
        self.assertTrue(remito)
        self.assertTrue(remito["pdf"])

    @unittest.skipIf(not MOCK, "Mock desactivados")
    @mock.patch.object(suds.client.Client, '__new__')
    def test_envio_inexistente(self, fake_client):
        '''
        Pruebo que obtenga los links PDF para imprimir en caso de numero de
        envio inexistente.
        '''
        # creo un cliente suds falso
        client = suds.client.Client('fake_url')
        # el cliente falso retornará error
        client.service.GeneracionRemitodeImposicion.side_effect = (
            suds.WebFault(type("testclass", (object,), {
                "Reason": type("testclass", (object,), {
                               "Text": """No se pudo generar la constancia,
                               por favor reintente en unos minutos """}),
            })(), None))
        fake_client.return_value = client
        with self.assertRaises(andreani.APIError):
            self.andreani.generar_remito_imposicion("*10000000249801")


class UltimoEstadoDistribucionTests(TestCase):
    '''
    Set de pruebas de obtener ultimo estado de distribucion
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_ingresado(self):
        '''
        Pruebo que obtenga el ultimo estado de distribucion para un envio
        ingresado al circuito de distribucion andreani.
        '''
        if MOCK:
            # configuro respuesta del mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(
                    dict={"Piezas": [
                        Factory.object(dict={"Pieza":
                            Factory.object(dict={
                                "NroPieza": "123456780a",
                                "NroAndreani": "*00000000249801",
                                "Estado": "Entregada",
                                "Fecha": "2012-01-01T00:00:00.00-00:00",
                                "Motivo": None,
                            })
                        })
                    ]}
                )
            )
        estado = self.andreani.consulta_ultimo_estado_distribucion(
            "*00000000249801")
        self.assertTrue(estado)


class DatosImpresionTests(TestCase):
    '''
    Set de pruebas de consultar datos de impresion
    '''
    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE)
        self.andreani.DEBUG = True

    def test_ingresado(self):
        '''
        Pruebo que obtenga el ultimo estado de distribucion para un envio
        ingresado al circuito de distribucion andreani.
        '''
        if MOCK:
            # configuro respuesta del mock
            self.andreani._API__soap = mock.MagicMock(
                return_value=Factory.object(
                    dict={'ResultadoConsultarDatosDeImpresion': [
                        dict(Categoria="Estandar",
                             CodigoDeResultado=1,
                             FechaDeRendicion=None,
                             FechaDeVencimientoDePrimerVisita=None,
                             FechasPactadas=None,
                             IdCliente="103",
                             NumeroAndreani="*00000000249801",
                             NumeroDePermisionaria="RNPSP Nº 586",
                             SucursalDeDistribucion="BAHIA BLANCA",
                             SucursalDeRendicion="0",
                        )]}))
        datos = self.andreani.consultar_datos_impresion("*00000000249801")
        self.assertTrue(datos)


class IntegrationTests(TestCase):
    '''
    Pruebas de integración del módulo.
    '''

    def setUp(self):
        self.andreani = andreani.API(TEST_USER,
                                     TEST_PASSWD,
                                     CLIENTE,
                                     CONTRATO_SUCURSAL)
        self.andreani.DEBUG = True

    @unittest.skipIf(MOCK, "Prueba debe realizarse sin mocks")
    def test_compra(self):
        '''
        Prueba circuito de compra de un cliente.
        '''
        # comprador consulta sucursales disponibles para retirar
        sucursales = self.andreani.consultar_sucursales()
        self.assertTrue(sucursales)
        # comprador elije sucursal
        sucursal = sucursales[0]["sucursal"]
        self.assertTrue(sucursal)
        # comprador solicita cotizacion del envio
        cotizacion = self.andreani.cotizar_envio(sucursal_retiro=sucursal,
                                                 cp_destino="1754",
                                                 peso="1000",
                                                 contrato="AND00EST",
                                                 volumen="1000")
        self.assertTrue(cotizacion)
        # comprador acepta tarifa y comfirma la compra llenando sus datos
        # personales
        compra = self.andreani.confirmar_compra(
            sucursal_retiro=sucursal,
            provincia="Buenos Aires",
            localidad="San Justo",
            codigo_postal=1754,
            calle="Florencio Varela",
            numero="1903",
            nombre_apellido="Elsa Pato",
            tipo_documento="DNI",
            numero_documento="12345678",
            email="email@example.com",
            numero_celular="1515151111",
            numero_telefono="43211234",
            detalle_productos_entrega="Prueba de entrega",
            detalle_productos_retiro="Prueba de envio",
            peso=1000,
            volumen=1000,
            contrato="AND00EST",
            tarifa=cotizacion["tarifa"]
        )
        self.assertTrue(compra)

    @unittest.skipIf(MOCK, "Prueba debe realizarse sin mocks")
    def test_impresion(self):
        '''
        Prueba circuito de impresion de etiquetas y remitos de imposicion.
        '''
        # vendedor consulta ventas para imprimir etiquetas
        ventas = self.andreani.reporte_envios_pendientes_impresion()
        self.assertTrue(ventas)
        # vendedor selecciona una venta e imprime etiqueta para el paquete
        venta = ventas[0]
        pdf = self.andreani.imprimir_constancia(venta["numero_andreani"])
        self.assertTrue(pdf)
        # vendedor consulta ventas para enviar a andreani
        ventas = self.andreani.reporte_envios_pendientes_ingreso()
        self.assertTrue(ventas)
        # vendedor selecciona piezas e imprime remito de imposicion
        pieza = ventas[0]
        self.assertTrue(pieza)
        remito = self.andreani.generar_remito_imposicion(
            pieza["numero_andreani"])
        self.assertTrue(remito)

    @unittest.skipIf(MOCK, "Prueba debe realizarse sin mocks")
    def test_anular(self):
        '''
        Prueba circuito de anulacion de envios.
        '''
        # vendedor consulta envios pendientes de ingreso al circuito operativo
        # andreani, es decir, que el paquete no se despachó en la sucursal
        # Andreani
        ventas = self.andreani.reporte_envios_pendientes_ingreso()
        self.assertTrue(ventas)
        # vendedor selecciona pieza para anular
        pieza = ventas[0]
        self.assertTrue(pieza)
        print(pieza)
        # vendedor anula envio
        respuesta = self.andreani.anular_envio(pieza["numero_andreani"])
        self.assertTrue(respuesta)
        print(respuesta)
