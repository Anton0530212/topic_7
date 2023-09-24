# num: int = int(input('Введите число: '))
# if num >= 0:
#     factorial = 1
#     while 1 < num + 1:
#         factorial *= num
#         num -= 1
#     print(factorial)
# else:
#     print('Факториал определен только для натуральных чисел.')
# не пойму почему факториал начинается с одгого
# и почему 1 отнимается от num - идет в обратном порядке

num: int = int(input('Введите число: '))
if num >= 0:
    for i in range(1, num + 1):
        num *= i
    print(num)
else:
    print('Факториал определен только для натуральных чисел.')
