#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("Введите число: "))
my_list = [0]
count = 1
if num > 0:
    my_list = [1, 0, 1]
while(count < num):
    my_list.append(my_list[len(my_list)-1]+my_list[len(my_list)-2])
    if count % 2 == 0:
        my_list.insert(0, my_list[len(my_list)-1])
    else:
         my_list.insert(0, my_list[len(my_list)-1])
    count +=1
print(my_list)         
