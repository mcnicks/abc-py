

def deco(x):
    print('deco', x)
    #return fx
    def outter(fx):
        print('outter', x, fx)
        def inner(*args, **kwargs):
            print('inner', *args, **kwargs)
            return fx(*args, **kwargs)
        return inner
    return outter


@deco(5)
def mainf(x):
    print('main function', x)

mainf(1)