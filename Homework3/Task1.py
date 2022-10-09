#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def inp_int(msg=""):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Некоректный ввод")
        else:
            return result        


def inp_int_list():
     count = input("Введите кличество элементов списка: ")
     result = []
     for i in range(count):
       result.append(input(f"Введите целое число {i+1}: "))
     return result


def sum_odd(num_list):
    result = 0
    for i in range(len(num_list)):
        if i % 2 == 1:
            result += num_list[i]
    return result

print(sum_odd(inp_int_list()))            