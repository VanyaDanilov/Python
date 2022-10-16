#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from itertools import count


n = int(input('Введите число: '))
list = []
for i in range(2,n + 1):
    if n % i == 0:
        count = 1
        for j in range(2,(i // 2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            list.append(i)
print(list)               