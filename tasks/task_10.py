num_1: int = int(input('Введите начало диапазона: '))
num_2: int = int(input('Введите конец диапазона: '))

if num_1 > num_2:
    num_1, num_2 = num_2, num_1
    for i in range(num_1, num_2, + 2):
        print(i)