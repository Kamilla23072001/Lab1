from random import randint
def func(n):
    mass = [[randint (0, 10) for i in range(n)] for j in range(n)]
    for i in mass:
        print(i)
func(4)