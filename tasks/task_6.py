number: int = abs(int(input('Введите целое число: ')))

count: int = 0
if number == 0:
    count = 1

if number < 0:
    number = abs(number)

while number > 0:
    count += 1
    number = number // 10

print("Количество цифр в числе:", count)
