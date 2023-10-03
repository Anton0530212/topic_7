start_num: int = int(input('Введите начало диапазона: '))
end_num: int = int(input('Введите конец диапазона: '))

if start_num > end_num:
    start_num, end_num = end_num, start_num

for num in range(start_num, end_num + 1):
    if num % 2 == 0:
        print(num)
    elif start_num == end_num:
        print(0)
