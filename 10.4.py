import random

number=random.randint(1, 10)

while True:
    tryes = input("Введите число или 'закончить' для выхода: ")
    if tryes == "закончить":
        break
    elif int(tryes) == number:
        print('Верно!')
        break
    elif int(tryes) <= number:
        print('Число меньше загадонного')
    elif int(tryes) >= number:
        print('Число больше загадонного')
    
