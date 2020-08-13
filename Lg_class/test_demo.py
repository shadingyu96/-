import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./Date.yaml")))
    def test_a(self, a, b):
        assert a + b


class TestDemo2:

    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def test_b(self, env):
        if "test" in env:
            print(f"这是一个测试环境{env['test']}")
        elif "dev" in env:
            print(f"这是一个开发环境{env['dev']}")


if __name__ == '__main__':
    pytest.main(["test_demo.py::TestDemo", "-v"])
