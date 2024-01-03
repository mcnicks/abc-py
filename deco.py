

def deco(x):
    print('deco', x)
    #return fx
    def outter(fx):
        print('outter', x, fx)
        return fx
    return outter


@deco(5)
def mainf(x):
    print('main function', x)

mainf(1)