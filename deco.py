

def deco(x):    # main deco, receives argument for deco
    print('deco', x)
    def outter(fx):     #outter deco, receives function
        print('outter', x, fx)
        def inner(*args, **kwargs):     # inner deco, receives arguments for func
            print('inner', *args, **kwargs)
            return fx(*args, **kwargs)
        return inner
    return outter


@deco(5)
def mainf(x):
    print('main function', x)

mainf(1)