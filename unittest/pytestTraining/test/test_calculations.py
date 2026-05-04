
import pytest

from src.calculations import Calculations

class TestClculations:
    calc = Calculations()


    @pytest.mark.parametrize("n1, n2, exval,", [(5, 5, 10), (-5, -5, -10 ), (0,5, 5)])

    def test_add(self, n1, n2, exval):
        res = self.calc.add(n1=10, n2=5)
        assert res == 15, 'Addition err'

    def test_sub(self):
        res = self.calc.sub(n1=10, n2=5)
        assert res == 5, 'subtraction err'

    def test_mul(self):
        res = self.calc.mul(n1=10, n2=5)
        assert res == 50, 'Multiplication err'

    @pytest.mark.skip(reason = 'Not I Yet')
    def test_div(self):
        res = self.calc.div(n1=10, n2=5)
        assert res == 2.0, 'Division Err'

    def test_ne(self):
        res = self.calc.ne(n1=10, n2= 10)
        assert res == True, 'NE'


    def test_driver(self):
        with pytest.raises( ZeroDivisionError):
            self.calc.div(10, 0)
