def fabonacci(N, a=0, b=1):
    L = []
    while len(L) < N:
        a, b = b, b+a
        L.append(a)
    return L


print(fabonacci(12))
print(fabonacci(12, 1, 3))


def catch_all(*args, **kwargs):
    print("args= ", args)
    print("kwargs= ", kwargs)


catch_all(1, 2, 3, a='a', b='b')
catch_all(1, 2, a='a')
cc = (1, 2, 4)
dd = {'aaa': 1234, 'asd': 22}
catch_all(cc, dd)
catch_all(*cc, **dd)


def add(x, y): return x+y


print(add(1, 6))

data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Hopper', 'YOB': 1906},
        {'first': 'Alan', 'last': 'Turing', 'YOB': 1912}]

print(sorted(data, key= lambda item: item['first']))
