num: int = int(input('Введите число: '))

if num > 1:
    for i in range(1, 5):
        print('Сумма всех чисел от 1 до', num, 'равна:', i * num)
else:
    print('Число должно быть больше или равно 1')

# ---------------

if num <= 1:
    print('Число должно быть больше или равно 1')
else:
    for i in range(1, 5):
        print('Сумма всех чисел от 1 до', num, 'равна:', i * num)
