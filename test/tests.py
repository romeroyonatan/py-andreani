import logging

from unittest import TestCase
from andreani.andreani import Andreani

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

logging.basicConfig(filename='testing.log', level=logging.DEBUG)


class AndreaniTests(TestCase):

    def test_consultar_sucursales(self):
        andreani = Andreani(TEST_USER, TEST_PASSWD, CLIENTE, CONTRATO_SUCURSAL)
        sucursales = andreani.consulta_sucursales(codigo_postal=1048)
        self.assertTrue(sucursales)
        sucursales = andreani.consulta_sucursales()
        self.assertTrue(sucursales)

    def test_cotizar_envio(self):
        andreani = Andreani(TEST_USER, TEST_PASSWD, CLIENTE, CONTRATO_SUCURSAL)
        andreani.cotizar_envio(sucursal_retiro="1",
                               cp_destino="1048",
                               peso="100",
                               volumen="100")
        self.assertTrue(False)
