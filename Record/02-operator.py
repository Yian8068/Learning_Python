
a = 2 ** 3

print(a, 2+3, 3**2)
print(-a, a % 3, a % 2)
print(a / 3, a // 3)


b = [1, 2]
c = [3, 4]
# print(b@c)

bin4 = bin(4)
bin10 = bin(10)
b4 = 4
b10 = 10

print(b4, b10)
print('& ', b4 & b10)
print('| ', b4 | b10)
print('^ ', b4 ^ b10)
print('<< ', b4 << b10)  # 0001 0000 0000 0000
print('>> ', b4 >> b10)
print('~ ', ~b4, ~b10)

print(1 < b4 < b10)
print(1 in [1, 2, 3])
print(11 not in [1, 2, 3])

aa = [1, 2, 3]
bb = [1, 2, 3]
print('aa:', aa, 'bb:', bb)
print('aa == bb ', aa == bb)
print(aa is bb)
