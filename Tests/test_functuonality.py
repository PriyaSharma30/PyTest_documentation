from Development.Program1 import *
import pytest

@pytest.mark.usefixtures('greeting')
class TestFunc:
    def test_palindrom(self):
        num1=pall_num(151)
        assert num1== 151, f'{num1} is not palindrom'
        pass

    def test_addition(self):
        num = add_sum(5,10)
        assert num == 15

    def test_amrstrong(self):
        num2=arms_num(153)
        assert num2==153 , f'{num2} is npt armstome number'
        pass

    def test_factorial(self):
        num3= fact(5)
        assert num3 ==120 , f'{num3} is not factorial'
        pass