#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

def Inp_Num(text):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Некоректный ввод")
    return number


def Sum_num(num):
    sum = 0
    for i in str(num):
        if i !=".":
            sum += int(i)
    return sum


num = Inp_Num("Введите число: ")

print(f"Сумма цифр = {Sum_num(num)}")