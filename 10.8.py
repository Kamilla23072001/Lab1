string = input("Введите строку")
maxword = 0
for i in string.split(' '):
    if len(i) > maxword:
        maxword = len(i)
        word = i
print("Самое длинное слово в строке:", word)



