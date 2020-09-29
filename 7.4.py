import random
num = random.randint(1,10)
while True:
    tryes = int(input('Введите число:'))
    if tryes == num:
        print('Победа')
        break
    else:
        print('Повторите еще раз')

"""Прогрмма загадывает случайное число лт 1 до 10 и дает пользователю его отгадать"""
       
