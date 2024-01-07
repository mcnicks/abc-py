
class TestClass:
    int_a = 1

    @classmethod
    def set_a(cls, a):
        cls.int_a = a

    @staticmethod
    def check_a(a):
        return bool(a)
    def update_a(self, a):
        self.a = a

    def __init__(self):
        pass

