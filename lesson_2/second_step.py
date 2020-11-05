items_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
number = 0
while i < items_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list) / 2)):
    my_list[number], my_list[number + 1] = my_list[number + 1], my_list[number]
    number += 2
print(my_list)
