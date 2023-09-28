start_num: int = int(input('Введите начало диапазона: '))
end_num: int = int(input('Введите конец диапазона: '))

if start_num > end_num:
    start_num, end_num = end_num, start_num

if start_num == end_num:
    if start_num % 2 == 0:
        print(start_num)
    else:
        print(0)
else:
    for num in range(start_num, end_num + 1):
        if num % 2 == 0:
            print(num)
