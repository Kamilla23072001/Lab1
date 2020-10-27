from random import randint
def func(n, m):
    mass = [[randint (0, 10) for i in range(n)] for j in range(m)]
    for i in mass:
        print(i)
func(5, 6)