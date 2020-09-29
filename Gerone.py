import math
def square(a, b, c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

if __name__ == "__main__":
    a,b,c = map(float, input('Введите значения сторон треугольника:').split())
    print('Площадь треугольника =', square(a, b, c))
    
"""Функция вычисляет площадь треугольника по формуле Герона"""
