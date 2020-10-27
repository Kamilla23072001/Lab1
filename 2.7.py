def Day(K):
    res = (K%7)+1
    return res

K = int(input('Введите целое число от 1 до 365:'))
res = Day(K)
print('Номер дня недели =', res)
