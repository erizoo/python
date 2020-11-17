from itertools import cycle

count = 0
my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    if count == 10:
        break
    print(el)
    count += 1
