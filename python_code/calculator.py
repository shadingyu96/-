class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except Exception:
            return "异常"

    def sub(self, a, b):
        try:
            return a - b
        except Exception:
            return "异常"

    def mul(self, a, b):
        try:
            return a * b
        except Exception:
            return "异常"


    def div(self, a, b):
        try:
            return a / b
        except Exception:
            return "异常"



if __name__ == '__main__':
    pass
