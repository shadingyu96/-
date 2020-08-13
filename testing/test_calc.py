import pytest
import yaml

from Shadingyu.python_code.calculator import *


def get_data():
    with open("Data/data.yaml", encoding="utf-8") as f:
        my_data = yaml.safe_load(f)
        add_data = my_data["Data"]["add"]
        id_data = my_data["Data"]["myids"]
        add_data2 = my_data["Data"]["add_float"]
        add_data3 = my_data["Data"]["add_Special"]
        div_data = my_data["Data"]["div"]
        div_data2 = my_data["Data"]["div_Special"]
        return [add_data, id_data, add_data2, add_data3, div_data, div_data2]


class TestDemo:
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("计算开始")

    @pytest.mark.add
    @pytest.mark.parametrize("a, b, expect", get_data()[0], ids=get_data()[1])
    def test_add(self, a, b, expect):
        """
        测试整数、零、字符、负数、大数相加
        :param expect: 预计结果
        :param a:第一位加数
        :param b:第二位加数

        """
        print("测试相加")
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.add
    @pytest.mark.parametrize("a, b, expect", get_data()[2])
    def test_add_float(self, a, b, expect):
        print("测试浮点数相加")
        result = round(self.calc.add(a, b), 1)
        assert expect == result

    @pytest.mark.add
    @pytest.mark.parametrize("a, b, expect", get_data()[3])
    def test_add_str(self, a, b, expect):
        print("测试非数字相加")
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.div
    @pytest.mark.parametrize("a, b, expect", get_data()[4])
    def test_div(self, a, b, expect):
        """"""
        print("测试数字相除")
        result = self.calc.div(a, b)
        assert expect == result

    @pytest.mark.div
    @pytest.mark.parametrize("a, b, expect", get_data()[5])
    def test_div_str(self, a, b, expect):
        print("测试非数字相除")
        result = self.calc.div(a, b)
        assert expect == result

    def teardown(self):
        print("计算结束")

    def teardown_class(self):
        pass
