#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def Sum_num(num):
    return num.isdigit()

num = None

while not  Sum_num(str(num)):
    num = input("Введите число n = ")
num = int(num) 

result = dict()
for i in range(1, num+1):
    result[i] = round((1+1/i)**i)

sums = 0
for i in result:
    sums += result[i]

print(result)        