rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('fourth_step_file_part_one.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])

with open('fourth_step_file_part_two.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
