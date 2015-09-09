import logging

from unittest import TestCase
from andreani.andreani import Andreani


TEST_USER = "eCommerce_Integra"
TEST_PASSWD = "passw0rd"

logging.basicConfig(filename='example.log',level=logging.DEBUG)

class TestAndreani(TestCase):
    def test_consultar_sucursales(self):
        andreani = Andreani(TEST_USER, TEST_PASSWD)
        andreani.consulta_sucursales()
        self.assertTrue(False)

