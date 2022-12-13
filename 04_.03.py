# HW04 Task 04
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# <Было>
# n = int(input("Введите число "))
# str1 = []
# if n==0:
#     str1.append(0)
# else:
#     while n>0:
#         str1.append(n%2)
#         n = n//2
# print(str1[::-1])

# <Стало>
def dec2bin(n):
    str1 = []
    if n==0:
        str1.append(0)
    else:
        while n>0:
            str1.append(n%2)
            n = n//2
    return(str1[::-1])
    
arr = [45,3,2]
lst = (list(map(dec2bin,arr)))
print(*list(zip(arr,lst)))