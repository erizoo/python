def my_sum():
    sum_res = 0
    ex = False
    while not ex:
        number = input('Введите строку чисел, разделенных пробелом или Q для выхода  - ').split()

        try:
            res = 0
            for el in range(len(number)):
                if number[el] == 'q' or number[el] == 'Q':
                    ex = True
                    break
                else:
                    res = res + int(number[el])
            sum_res = sum_res + res
            print(f'Текущая сумма {sum_res}')
            print(f'Финальная сумма {sum_res}')
        except ValueError:
            print('Неверный формат ввода')


my_sum()
