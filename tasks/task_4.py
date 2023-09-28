num: int = int(input('Введите число: '))

summa: int = 0

if num > 1:
    for i in range(1, num + 1):
        summa += i
    print('Сумма всех чисел от 1 до', num, 'равна:', summa)
elif num == 1:
    print(1)
else:
    print('Число должно быть больше или равно 1')
