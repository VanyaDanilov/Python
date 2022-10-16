#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета.
#Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
#За один ход можно забрать не более чем 28 конфет.
#Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

# вариант человек против бота c "интеллектом":
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил(а) {name}, он(а) взял(а) {k}, теперь у него(неё) {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = 2021
flag = randint(0,2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл(a) {player1}")
else:
    print(f"Выиграл(a) {player2}")