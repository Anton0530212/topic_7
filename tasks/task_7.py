num: int = int(input("Введите число: "))

divisor: int = 2

while num > 1:
    while num % divisor == 0:
        print(divisor, end=' ')
        num //= divisor
    divisor += 1

# ---------------
# Шох, признаюсь, не пойму я эту задачу и воспользовался GPT,
# он мне выдал код ниже, а из него я сделал решение выше

def find_prime_factors(num):
    prime_factors = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            prime_factors.append(divisor)
            num //= divisor
        divisor += 1

    return prime_factors


# Получаем число от пользователя
num = int(input("Введите число (больше 1): "))

# Вызываем функцию и выводим результат
result = find_prime_factors(num)
print("Простые множители:", " ".join(map(str, result)))