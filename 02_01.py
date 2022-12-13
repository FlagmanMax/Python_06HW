# HW_ 02_01

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# <БЫЛО>
# str1 = input("Введите число: ")
# sum = 0
# for i in range (len(str1)):
#     # if str1[i] in range('0','9'):
#     if ord(str1[i]) in range(48,58):
#         sum += int(str1[i])
# print(f"\nСумма цифр числа {str1} = {int(sum)}")

# <СТАЛО>, использовал функции map, filter, lambda
print(f"Сумма цифр = {sum(list(map(int,filter(lambda x: ord(x) in range(48,58),input('Введите число: ')))))}")
