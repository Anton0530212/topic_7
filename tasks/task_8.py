start_num: int = int(input('Введите начало диапазона: '))
end_num: int = int(input('Введите конец диапазона: '))

if start_num > end_num:  # Отлично!
    start_num, end_num = end_num, start_num

# Эти условия должны быть реализованы внутри цикла (в цикле будет только if elif)
if start_num == end_num:
    if start_num % 2 == 0:  # Это ты уже реализовал в цикле
        print(start_num)
    else:
        print(0)

for num in range(start_num, end_num + 1):
    if num % 2 == 0:  # Это правильно
        print(num)
    elif ...:
        ...
