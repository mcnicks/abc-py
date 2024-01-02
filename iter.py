

def myiter(a):

    for c in a:
        yield c



for c in myiter([100, 200, 300, 1, 2, 3, 1000]):
    print(c)