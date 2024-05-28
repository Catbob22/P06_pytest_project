from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a=5
        b=2
        cal= Calculator()

        result= cal.subtract(a,b)

        expected=3
        assert result==expected

    def test_multiply(self):
        a=2
        b=4
        cal= Calculator()

        result = cal.multiply(a,b)

        expected=8
        assert result==expected

    def test_divide(self):
        a=10
        b=2
        cal= Calculator()

        result= cal.divide(a,b)

        expected=5
        assert result==expected

    def test_divide_by_zero(self):
        a= 10
        b=0
        cal= Calculator()

        with pytest.raises(ZeroDivisionError, match="Division by zero error"):
            cal.divide(a, b)