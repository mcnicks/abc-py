class TestDescr:

    def __set_name__(self, owner, name):
        self.name = '_' + name
        print(f'{self.name=}')

    def __set__(self, instance, value):
        print(f'setter: {value=}')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print(f'getter: {self.name=}')
        return instance.__dict__[self.name]


class TestClass:
    int_a = 1

    desc_a = TestDescr()

    @classmethod
    def set_a(cls, a):
        cls.int_a = a

    @staticmethod
    def check_a(a):
        return bool(a)
    def update_a(self, a):
        self.a = a

    def __init__(self, a):
        self.a = a
        self.desc_a = a

e = TestClass(5)
print(e.desc_a)