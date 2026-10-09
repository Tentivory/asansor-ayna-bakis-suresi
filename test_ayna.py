import unittest
from ayna_bakis import teshis_ver, muhur_ozeti


class TestAyna(unittest.TestCase):
    def test_kisa_bakis(self):
        metin, _, puan = teshis_ver(0.4, 0, False)
        self.assertIn("Profesyonel", metin)
        self.assertLess(puan, 20)

    def test_yolcu_agirlastirir(self):
        _, _, yalniz = teshis_ver(3.0, 0, False)
        _, _, kalabalik = teshis_ver(3.0, 2, False)
        self.assertGreater(kalabalik, yalniz)

    def test_muhur_sabit(self):
        self.assertEqual(len(muhur_ozeti()), 12)


if __name__ == "__main__":
    unittest.main()
