from unittest import TestCase

from Kalkulacka1 import Kalkulacka

class TestKalkulacka(TestCase):
    def test_scitani(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(5, kalkulacka.scitani(2, 3))
        self.assertEqual(-3, kalkulacka.scitani(-7, 4))
        self.assertEqual(5, kalkulacka.scitani(-5, 10))

    def test_odcitani(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(5, kalkulacka.odcitani(5, 3))
        self.assertEqual(-3, kalkulacka.odcitani(-7, 4))
        self.assertEqual(5, kalkulacka.odcitani(12, 10))

    def test_nasobeni(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(5, kalkulacka.nasobeni(2, 3))
        self.assertEqual(-3, kalkulacka.nasobeni(-7, 4))
        self.assertEqual(5, kalkulacka.nasobeni(-5, 10))

    def test_deleni(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(5, kalkulacka.deleni(10, 3))
        self.assertEqual(-3, kalkulacka.deleni(8, 4))
        self.assertEqual(5, kalkulacka.deleni(20, 2))
