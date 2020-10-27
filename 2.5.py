def Func(a1,b1,c1,a2,b2,c2):
    d=a1*b2-a2*b1
    x=(c1*b2-c2*b1)/d
    y=(a1*c2-a2*c1)/d
    return x,y

a1= int(input('Введите a1:'))
b1= int(input('Введите b1:'))
c1= int(input('Введите c1:'))
a2= int(input('Введите a2:'))
b2= int(input('Введите b2:'))
c2= int(input('Введите c2:'))

res = Func(a1,b1,c1,a2,b2,c2)
print('Решение: x,y =', res )
