import math
def f (x,y):
    z = round((x+(2+y)/x**2)/(y+1/ math.sqrt(x**2+10)),2)
    q = round(2.8*math.sin(x)+abs(y),2)
    return z,q

x = float(input('Введите значение x:'))
y = float(input('Введите значение y:'))
z,q = f(x,y)
print('Значение z и q:', z, q)

"""Программа вычисляет значения z и q по введенным значениям x и y"""
