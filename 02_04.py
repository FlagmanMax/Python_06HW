# # Seminar 2 Task 04

# # Вводятся 2 строки, каждая с новой строчки
# # Из первой выделить все четные символы
# # из второй - с нечетными. Объединить и вывести

# <Было>
# str1 = input("Введите строку 1: ")
# str2 = input("Введите строку 2: ")
# for i in range(0,len(str1)-1):
#     if i%2==0:
#         print(str1[i], end = "")
# # print(" ")
# for i in range(0,len(str2)-1):
#     if i%2==1:
#         print(str2[i], end = "")

# <Стало>
str1 = input('Введите строку 1: ')
str2 = input('Введите строку 2: ')
print(*list(zip(str2[0::2], str1[1::2])))