from src.calculations import Calculations


class TestClac:
    calc = Calculations()

    def test_area_of_suare(self):
        res = self.calc.area_of_square(10)
        assert res == 100, 'Area is wrong'

    def test_peri_of_rect(self):
        res = self.calc.peri_of_rect(10,5)
        assert res == 30, 'Peri is wrong'