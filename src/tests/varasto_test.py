import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)


    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_konstruktori_tayttaa_liian_suuren_alkusaldon(self):
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_ei_lisaa_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_tayttaa_varaston_jos_maara_on_liian_suuri(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_ei_ota_negatiivista_maaraa(self):
        saatu = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_palauttaa_koko_saldon_jos_pyynto_on_liian_suuri(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_varaston_tiedot(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_ottaminen_tasmalleen_koko_saldo(self):
        self.varasto.lisaa_varastoon(10)

        saatu = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu, 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
