def Time(n):
    sec = n%3600
    min = sec//60
    return min

n = int(input('Введите количество секунд:'))
res = Time(n)
print('Количество полных минут, прошедших с начала последнего часа =', res)
