# coding:utf-8
print(type('11111'))
print(type(11111))
print(type(1111.1))
print(type(None))

x = 0.0004
y = 4e-4
print(x == y)


print(float(1))

# 精度
print(0.1 + 0.2 == 0.3)
# 避免比較浮點數

i = complex(3, 4)
print(i, abs(i), i.real, i.imag)

aa = "aaa asd"
bb = 'bbbkd'


print(len(aa), aa[0], aa*6, aa.upper(), aa+bb, aa.title())

# Boolean 開頭字母必須大寫
true = True
false = False
print("bool(0): ", bool(0))
print("bool(1234): ", bool(1234))
print("bool(None): ", bool(None))
print("bool(""): ", bool(""))
print("bool(\"None\"): ", bool("None"))
print("bool([]): ", bool([]))
print("bool([1,2,3]): ", bool([1, 2, 3]))
