from itertools import count

n1 = (n**2 for n in range(12))
print(n1)
print(list(n1))

# Generator, is not a list of value but a method of generate value.
# So, it does not cost a lot of memory to put a list in.
n1 = (n**2 for n in range(12))
for i in n1:
    print("i:", i)


for x in count(2, 2):
    print(x, end=" ")
    if x > 30:
        break
print("")

factors = [2, 3, 5, 7]
G = (i for i in count() if all(i % n > 0 for n in factors))
for val in G:
    print(val, end=' ')
    if val > 40:
        break
print("")

G = (n**2 for n in range(12))
for n in G:
    print(n, end=' ')
    if n > 30:
        break

print("\ndoing something in between")
for n in G:
    print(n, end=' ')
print("")

