seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month = int(input("Введите месяц по номеру "))
if month in seasons_dict['Зима']:
    print('Зима')
elif month in seasons_dict['Весна']:
    print('Весна')
elif month in seasons_dict['Лето']:
    print('Лето')
elif month in seasons_dict['Осень']:
    print('Осень')
else:
    print("Такого месяца не существует")
