from itertools import count

number = int(input('Введите стартовое число '))
for el in count(number):
    print(el)
    if el == number + 100:
        break
