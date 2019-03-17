
G1 = (n ** 2 for n in range(12))

# yield : return a sequence contains infinity value


def gen():
    for n in range(12):
        yield n ** 2


G2 = gen()
print(*G1)
print(*G2)

L = [n for n in (range(2, 40))]
L = [n for n in L if n == L[0] or n % L[0] > 0]
L = [n for n in L if n == L[1] or n % L[1] > 0]
L = [n for n in L if n == L[2] or n % L[2] > 0]

print(L)


def get_primes(N):
    primes = set()
    for i in range(2, N):
        if all(i % p > 0 for p in primes):
            primes.add(i)
            yield i

print(*get_primes(100))