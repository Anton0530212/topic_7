# Программа, которая запрашивает у пользователя число и
# выводит на экран факториал этого числа.
num: int = int(input('Введите число: '))

summa: int = 1

if num >= 0 or num == 0:
    for i in range(1, num + 1):
        summa *= i
    print('Факториал числа', num, 'равен', summa)
else:
    print('Факториал определен только для натуральных чисел.')


# --------------------------


if num < 0:
    print("Факториал определен только для натуральных чисел.")
else:
    factorial: int = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Факториал числа", num, "равен", factorial)



