class TestClass():

    d = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

        type(self).d = a + b

    @classmethod
    def opend(cls):
        print(cls.d)

    @staticmethod
    def statopen(a, b):
        return a + b

TestClass.opend()
a = TestClass(2, 3)

TestClass.opend()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
