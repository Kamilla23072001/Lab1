string = input("Введите строку")
numbers = []
for i in string:
    if i in '1234567890':
        numbers.append(int(i))
print("Все цифры в строке:", numbers)
print("Количество цифр в строке:", len(numbers))
print("Сумма цифр в строке:", sum(numbers))
print("Максимальная цифра в строке:", max(numbers))