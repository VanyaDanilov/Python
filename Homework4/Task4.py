#Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def generate_superscript(x, n):
   if n == 0:
      return str(x)
   if n == 1:
      return str(x)+"x"
   superscript = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
   result = str(x)
   if x != 0:
      result += "x"
   for i in str(n):
      result += superscript[int(i)]
      return result

def generate_polynomial(k):
     result = []
     for i in range(k, -1, -1):
         coefficient = random.randint(0, 10)
         if coefficient != 0:
           result.append(generate_superscript(coefficient, i))
     return "+".join(result)


print(generate_polynomial(10))