num: int = int(input("Введите число: "))

primes: list = []

for i in range(2, num + 1):
    while num % i == 0:
        primes.append(i)
        num /= i

print(" ".join(map(str, primes)))