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


    def test_sub(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_mul(self):
        # arrange
        a = 43
        b = 6
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 258
        assert result == expected

    def test_div(self):

        a = 500
        b = 5
        cal = Calculator()

        result = cal.divide(a, b)

        with pytest.raises(ZeroDivisionError, match="Division by zero error"):
            cal.divide(a, b)


