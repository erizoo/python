try:
    with open('fifth_step_file.txt', 'w+') as file_obj:
        line = input('Введите цифры через пробел \n')
        file_obj.writelines(line)
        my_numb = line.split()

        print(f"Сумма чисел равна {sum(map(int, my_numb))}")
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Неправильно набран номер. Ошибка ввода-вывода')
