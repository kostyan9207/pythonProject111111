mport pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multip_calculator_positive(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multip_calculator_negative (self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculator_positive(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_division_calculator_negative(self):
        assert self.calc.division(self, 2, 2) == 0

    def test_substruction_calculator_positive(self):
        assert self.calc.substruction(self, 3, 2) == 1

    def test_substruction_calculator_negative(self):
        assert self.calc.substruction(self, 3, 2) == 0

    def test_adding_calculator_positive(self):
        assert self.calc.adding(self, 3, 2) == 5

    def test_adding_calculator_negative(self):
        assert self.calc.adding(self, 3, 2) == 4
