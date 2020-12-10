from time import sleep

import allure
import pytest


class TestDemo:
    @allure.testcase("http://www.sardine.icu")
    @allure.feature("测试计算机加法")
    @pytest.mark.flaky(reruns = 5)
    # @pytest.mark.parametrize("a, b, expect", get_data()[0], ids=get_data()[1])
    def test_add(self, calc, get_add_data):
        """
        测试整数、零、字符、负数、大数相加
        :param expect: 预计结果
        :param a:第一位加数
        :param b:第二位加数

        """
        with allure.step("输出测试相加"):
            print("测试相加")
        # sleep(1)
        with allure.step("测试相加开始"):
            result = calc.add(get_add_data[0], get_add_data[1])
        with allure.step("测试相加开始"):
            assert get_add_data[2]== result
            # pytest.assume(2 == 4)
            # pytest.assume(3 == 4)


    # @pytest.mark.add
    # @pytest.mark.parametrize("a, b, expect", get_data()[2])
    def test_add_float(self, calc, get_add_float_data):
        print("测试浮点数相加")
        result = round(calc.add(get_add_float_data[0], get_add_float_data[1]), 1)
        assert get_add_float_data[2] == result

    # @pytest.mark.add
    # @pytest.mark.parametrize("a, b, expect", get_data()[3])
    def test_add_special(self, calc, get_add_special_data):
        print("测试异常数据相加")
        result = calc.add(get_add_special_data[0], get_add_special_data[1])
        assert get_add_special_data[2] == result

    # @pytest.mark.div
    # # @pytest.mark.parametrize("a, b, expect", get_data()[4])
    def test_div(self, calc, get_div_data):
        """"""
        print("测试数字相除")
        result = calc.div(get_div_data[0], get_div_data[1])
        assert get_div_data[2] == result

    # @pytest.mark.div
    # @pytest.mark.parametrize("a, b, expect", get_data()[5])
    def test_div_special(self, calc, get_div_special_data):
        print("测试非数字相除")
        result = calc.div(get_div_special_data[0], get_div_special_data[1])
        assert get_div_special_data[2] == result
