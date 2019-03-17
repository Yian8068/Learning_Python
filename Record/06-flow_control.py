if(1 > 2):
    print('1>2')
elif(1 == 2):
    print('1=2')
else:
    print('1<2')

for a in [2, 4, 5, 6]:
    print(a**a)

for a in range(10):
    print(a**2)

for a in list(range(5, 10)):
    print(a**2)

i = 1

while i < 20:
    print((20-i+2)//2*' ', i*'*')
    i += 2

while i > 0:
    print((20-i+2)//2*' ', i*'*')
    i -= 2

# fibonacci

a = 0
b = 1
L = []
while True:
    (a, b) = (b, b+a)
    if a > 100:
        break
    L.append(a)
print(L)


# for-else
# like "finally"
fac = []
for i in range(2, 40):
    for f in fac:
        if(i % f == 0):
            break
    else:
        fac.append(i)
else:
    print(fac)
