num: float = float(input('Введите число: '))
if num > 1:
    for i in range(1, 5):
        print('Сумма всех чисел от 1 до', int(num), 'равна:', i * int(num))
else:
    print('Число должно быть больше или равно 1')