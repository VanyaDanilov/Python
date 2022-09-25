#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90



from random import randint
count = 20
num = [randint(1, 100) for i in range(count)]
print(num)
max_num = num[0]
min_num = num[0]
for i in range(count):
    if num[i] > max_num : max_num = num[i]
    if num[i] < min_num : min_num = num[i]
print('max_num:',max_num, 'min_num:',min_num)    

