from random import randint
def func(n, m):
    s = 0
    num = 0
    mass = [[randint (0, 10) for i in range(n)] for j in range(m)]
    for i in mass:
        print(i)
    for i in range(m):
        for j in range(n):
            s1=mass[i].count(mass[i][j])
            if s1>s:
                s=s1
                num=i
    print("Номер строки с максимальным числом одинаковых элементов =", num+1)

func(4, 3)