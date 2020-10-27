number = int(input("Введите число"))
sum = 0
for i in str(number):
    if int(i) % 2 != 0:
       sum += int(i)**2
print(sum)