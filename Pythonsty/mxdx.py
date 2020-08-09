class Person:
    def __init__(self, name):
        self.name = name


class Man(Person):
    def __init__(self, name):
        super().__init__(name)
        self.gender = "男"


class Women(Person):
    def __init__(self, name):
        super().__init__(name)
        self.gender = "女"


class Kid(Person):
    def __init__(self, name):
        super().__init__(name)
        self.age = "0-12岁"


class OldPeole(Person):
    def __init__(self, name):
        super().__init__(name)
        self.age = "60岁以上"

