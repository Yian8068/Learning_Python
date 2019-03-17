# List
a = [1, 2, 3]
print(a)
print(len(a))
b = a + [1, 4]
print(b)
b.sort()
print(b)
L = [1, 'two', 3.14, [0, 3, 5]]
print(L)
print("L[-1]: ", L[-1])
print("L[0:3]: ", L[0:3])
print("L[-2:]: ", L[-2:])
L.clear()
L = [1, 2, 3, 4, 6, 7]
print(L)
print("L[1]: ", L[1])
print("Get value from every 2 element=> L[::2] : ", L[::2])
print("DESCEND=> L[::-1]: ", L[::-1])
L[0] = 100
print(L)
L[2:4] = [1, 5]
print(L)

# Tuple
t = 1, 2, 3
print(t)
# can not be change
# t[0] = 5
x = 0.125
print(x.as_integer_ratio())
q, w = x.as_integer_ratio()
print(q / w)

# dictionary

t_dict = {'a': 's', 'b': 123}
t_dict['hh'] = (1, 2, 3)
print(t_dict)

# set
t_set = {1, 3, 5, 7}
t_set2 = {1, 2, 5, 7}
print(t_set.union(t_set2))
print(t_set & t_set2)
print(t_set ^ t_set2)
