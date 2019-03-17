# coding:utf-8
num = 5 
upper = []
lower = []

for i in range(10):
    if i >= num:
        upper.append(i)
    else:
        lower.append(i)
    print(i)

print("lower:", lower)
print("upper:", upper)

lower.clear()
upper.clear()
# 縮排影響

for i in range(10):
    if i >= num:
        upper.append(i)
    else:
        lower.append(i)
        print(i)

print("lower2:", lower)
print("upper2:", upper)


#測試換行
wrap1 = 1+2+3 +\
4
wrap2 = (1+2+3
         + 4)
print("wrap1:", wrap1)
print("wrap2:", wrap2)
