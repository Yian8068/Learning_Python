
# assign variable is like a pointer (address reference)
x = 4

x = 'aaa'

x = [1, 2, 3]

y = x  # same reference

print(x, y)

y.append(4)

print(x, y)

y = 'asdasda'

print(x, y)

x = 10
y = x
x += 5  # 把 x 的值加上 5 再賦給 x
print("x =", x)
print("y =", y)
