import os
from typing import List
import pytest
import yaml

from Shadingyu.python_code.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope="module")
def calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


def get_data():
    my_file = os.path.dirname(__file__) + "/Data/data.yaml"
    with open(my_file, encoding="utf-8") as f:
        my_data = yaml.safe_load(f)
        # add_data = my_data["add"]["datas"]
        # add_ids = my_data["add"]["myids"]
        # add_float_data = my_data["add_float"]["datas"]
        # add_float_ids = my_data["add_float"]["myids"]
        # add_Special_data = my_data["add_Special"]["datas"]
        # # div_data = my_data["div"]["datas"]
        # # div_data2 = my_data["div_Special"]["datas"]
        # # return [add_data, add_ids, add_float_data, add_float_ids]
        return my_data


@pytest.fixture(params=get_data()["add"]["datas"], ids=get_data()["add"]["myids"])
def get_add_data(request):
    """获取加法数据"""
    return request.param


@pytest.fixture(params=get_data()["add_float"]["datas"], ids=get_data()["add_float"]["myids"])
def get_add_float_data(request):
    """获取浮点数加法数据"""
    return request.param


@pytest.fixture(params=get_data()["add_Special"]["datas"], ids=get_data()["add_Special"]["myids"])
def get_add_special_data(request):
    """获取异常数据加法数据"""
    return request.param


@pytest.fixture(params=get_data()["div"]["datas"], ids=get_data()["div"]["myids"])
def get_div_data(request):
    """获取除法数据"""
    return request.param


@pytest.fixture(params=get_data()["div_Special"]["datas"], ids=get_data()["div_Special"]["myids"])
def get_div_special_data(request):
    """获取异常除法数据"""
    return request.param
