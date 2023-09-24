print('Таблица умножения для числа 5 с помощью цикла for:')
num: int = int(input('Введите число: '))
for i in range(1, 11):
    print(num, '*', i, '=', num * i)

# ------------------

print('Таблица умножения для числа 5 с помощью цикла while:')
i = 0
while i < 10:
    i += 1
    print(num, '*', i, '=', num * i)
