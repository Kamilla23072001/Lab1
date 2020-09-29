import math
x = float(input('Введите значение x:'))

if x >= 0.2 and x <= 0.9:
    print('Значение функции=', round(math.sin(x),2))
else:
    print('Значение функции=', 1)

"""Программа вычисляет значение функции"""
