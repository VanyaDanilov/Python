#4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#Примеры:
#- 6,78 -> 7
#- 5 -> нет
#- 0,34 -> 3

from itertools import count


num = input('Введите число: ')
count = 0
not_num = 0
for i in num:
    count+=1
    if i == "," or i == ".":
        not_num = 1
        print(num[count])
if not_num == 0:
    print('Нет')        