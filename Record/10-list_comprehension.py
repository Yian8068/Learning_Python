L = []
for i in range(12):
    L.append(i**2)

print(L)

LC = [i**2 for i in range(12)]

print(LC)

# multiple for loop

ML = [(i, j) for i in range(5) for j in range(3)]
print(ML)


ML = [(i, j) for i in range(5) for j in range(3) if i > 2]
print(ML)

val = -10
print(val if val >= 0 else -val)

LS = {i**2 for i in range(12)}
print(LS)

LS = {str(i): i**2 for i in range(12)}
print(LS)
