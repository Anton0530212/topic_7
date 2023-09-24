# num: int = int(input('Введите целое число: '))
# total_gigit = 0
# while num > total_gigit:
#     total_gigit = total_gigit + num
#     num += 1
#     print(total_gigit - 1)

# user_input = int(input("Введите целое число: "))
# num = str(user_input).split(' ')
# for i in num:
#     print(num)

# for i in range(user_input + 1):
#     print(i, end=' ')


number: int = abs(int(input('Введите целое число: ')))
if number > 0:
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    print("Количество цифр в числе:", count)
else:
    print("Количество цифр в числе:", 1)

# ----------------------------

count: int = 0
if number == 0:
    count = 1
else:

    # if number < 0:
    #     number = abs(number)

    while number > 0:
        count += 1
        number = number // 10

print("Количество цифр в числе:", count)
