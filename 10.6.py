sum = 0
while True:
    text = input("Введите 'стоп' или введите число")
    if text == "стоп":
        break
    else:
        sum += int(text)
print("Сумма =", sum)
