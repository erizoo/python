profit = float(input("Введите выручку фирмы "))
material_losses = float(input("Введите издержки фирмы "))
if profit > material_losses:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / material_losses:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == material_losses:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
