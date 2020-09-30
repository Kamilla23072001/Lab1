L = [-8, 8, 6.0, 5, 'строка', -3.1]
sumL = 0
for i in range(0, len(L)):
    if type(L[i]) == int or type(L[i]) == float:
        sumL += L[i]
print(sumL)
