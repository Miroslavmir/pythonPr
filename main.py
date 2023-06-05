# result = 1
#
# while True:
#     number = int(input('Input number: '))
#     if number < 0:
#
#         continue
#     if number == 0:
#         break
#
#     result *= number
#     print(result)
# print('result =', result)

# resul = 0
# while True:
#     number = int(input('целое число : '))
#
#     if number == 0:
#         break
#         resul += number
#     print(resul)
# print( ' resul =', resul)

# resul = 0
# count = 0
# while True:
#     number = int(input('целое число : '))
#     if number >= 0:
#         resul += number
#         count += 1
#     if number < 0:
#         break
#
#     print('сумма ',resul)
# print(' resul =', resul / count)
result = 0
# while True:
#     number = int(input('целое число : '))
#
#     if number > 0 and number % 2 == 1 or number < 0 and number % 2 == 1:
#         result += number
#     if number == 0:
#         break
#
#     print('число =', result)
# print(' result =', result)

# 6.42. Дано натуральное число, в котором все цифры различны. Определить:
# а) порядковые номера двух его максимальных цифр, считая номера:
# от конца числа;
# от начала числа;
# def x_y_digits(num):
#     x_digit, min_pos = float("inf"), float("inf")
#     y_digit, max_pos = float("-inf"), float("-inf")
#     pos = 1
#     while num > 0:
#         digit = num % 10
#         if digit > y_digit:
#             y_digit = digit
#             y_pos = pos
#         if digit < x_digit:
#             x_digit = digit
#             x_pos = pos
#         num //= 10
#         pos += 1
#     return x_pos, y_pos
#
# print(x_y_digits(123456789))
# print(x_y_digits(123456789))
#
#
# number1 = 5
# number2 = 10
# summa = number1 + number2
# print(number1,'+', number2, '=', number1 + number2)

# number = int(input('введите число\n'))
# number1 = 0
# while number > 0:
#     num = number // 10
#     num2 = number // 10
#     num3 = number + 3
# summ = num
#
# number = int(input('введите число\n'))
# num1 = 0
# num2 = 0
# num3 = 0
# while number > 0
#     num = number % 10
#

# # дано предложение вывести количество слов в нем
# text = input('введите предложение')
# ndex = 0
# indexSyb = 1
# x = len(text)
# while ndex < x:
#     if text[ndex] == ' ':
#         indexSyb += 1
#     ndex += 1
# print(f'введите = {indexSyb}'s )

# s = 'hello world'
# print(s[::-1])

str = input('введите текст_\n')
s = input('введите текст\n')
print(str[:-1] + s)
