import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_negatiivisen_varaston(self):
        uusi_varasto = Varasto(-6)
        vastaus = uusi_varasto.tilavuus
        self.assertEqual(vastaus, 0) # rikottu testi, oikea vastaus on nolla, väärässä 16

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_alku_saldo_negatiivinen(self):
        uusi_varasto = Varasto(10, alku_saldo=-4)
        vastaus = uusi_varasto.saldo
        self.assertEqual(vastaus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisaa_varastoon_negatiivista(self):
        varasto_ennen_lisaysta = self.varasto.saldo
        self.varasto.lisaa_varastoon(-6)
        varasto_lisayksen_jalkeen = self.varasto.saldo
        self.assertEqual(varasto_ennen_lisaysta, varasto_lisayksen_jalkeen)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisaa_varastoon_liikaa(self):
        nyt_mahtuu = self.varasto.paljonko_mahtuu()
        liian_suuri_lisays = nyt_mahtuu + 5
        self.varasto.lisaa_varastoon(liian_suuri_lisays)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ota_varastosta_negatiivista(self):
        vastaus = self.varasto.ota_varastosta(-6)
        self.assertEqual(vastaus, 0)

    def test_ota_varastosta_liikaa(self):
        maksimi_otettavissa = self.varasto.saldo
        otetaan_liikaa = maksimi_otettavissa + 5
        vastaus = self.varasto.ota_varastosta(otetaan_liikaa)
        self.assertEqual(vastaus, maksimi_otettavissa)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_vastaus_oikein(self):
        saldo = self.varasto.saldo
        tilaa = self.varasto.paljonko_mahtuu()
        haluttu = f"saldo = {saldo}, vielä tilaa {tilaa}"
        vastaus = str(self.varasto)
        self.assertEqual(vastaus, haluttu)
        