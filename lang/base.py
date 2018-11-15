
def number():
    print("type(1): ", type(1)) # int
    print("type(-1): ", type(-1)) # int
    print("type(1.1): ", type(1.1)) # float
    print("type(1 * 1.0): ", type(1 * 1.0)) # float
    print("type(2/2): ", type(2/2)) # float
    print("type(2//2): ", type(2//2)) # int 整除

def group():
    g = [1, 2, -1, 4, 'a', True ]
    print('列表: ', type(g)) # list
    print(g[0])
    print(g[1:3])
    print(g[-1:]) # last
    print(g + ['c','d'])
    # print(g + ['c','d']) # error
    # print(g * ['c', 'd']) # error
    print(g * 3)


def vars():
    a = [1, 2, 3]
    b = [1, 2]
    print(a + b)
    c = a or b and a
    print(c)


if __name__ == '__main__':
    number()
    group()
    vars()