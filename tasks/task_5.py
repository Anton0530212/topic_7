num: int = int(input('Введите число: '))
if num >= 0:
    for i in range(1, num + 1):
        num *= i
    print(num)
else:
    print('Факториал определен только для натуральных чисел.')


# ---------------
# summa = 0
# for i in range(1, num + 1):
#     summa += i
#
# print(summa)
#
