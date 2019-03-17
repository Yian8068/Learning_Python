from itertools import permutations, combinations, product
L = [2, 4, 6, 8, 10]
for i in range(len(L)):
    print(i, L[i])
print()

for i, val in enumerate(L):
    print(i, val)
print()

L = [2, 4, 6, 8, 10]
R = [3, 6, 9, 12]
for lval, rval in zip(L, R):
    print(lval, rval)
    # the shortest list will define zip length
print()

# square = lambda x: x ** 2
for val in map(lambda x: x ** 2, range(10)):
    print(val, end=' ')
print()


def is_even(x): return x % 2 == 0


for val in filter(is_even, range(10)):
    print(val, end=' ')
print()
print(range(10))
print()
print(*range(10))
print()
L1 = (1, 2, 3, 4)
L2 = ('a', 'b', 'c', 'd')
z = zip(L1, L2)
print(z)
print(*z)

z = zip(L1, L2)
new_L1, new_L2 = zip(*z)
print(new_L1, new_L2)

z = zip(L1, L2)
for q, w, e, r in zip(*z):
    print(q, w, e, r)

z = zip(L1, L2)
for tup in zip(*z):
    print(tup)

z = zip(L1, L2)
for lval, ravl in z:
    print(lval, ravl)

pe = permutations([1, 2, 3])

print("pe:", *pe)

com = combinations(range(4), 2)
print("com:", *com)

p = product('ab', range(3))
print("p:",*p)