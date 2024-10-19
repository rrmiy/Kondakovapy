#Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном наборе.

import random

a = random.randrange(-3,3)
b = random.randrange(-3,3)
c = random.randrange(-3,3)
print("три числа:", a, b, c)

x = 0
if a > 0:
  x += 1
if b > 0:
  x += 1
if c > 0:
  x += 1
print("Количество положительных чисел: ",x)

y = 0
if a < 0:
  y += 1
if b < 0:
  y += 1
if c < 0:
  y += 1
print("Количество отрицательных чисел: ",y)