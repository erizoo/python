# a = int(input())
# m = a % 10
# a = a // 10
# while a > 0:
#     if a % 10 > m:
#         m = a % 10
#     a = a // 10
# print(m)
# a = 10
# b = 15
# print("Переменные a и b - ", a, b)
# first_string = input("Введите первую строку ")
# first_number = int(input("Введите первое число "))
# second_string = input("Введите вторую строку ")
# second_number = int(input("Введите второе число "))
# print("Введеные значения - %10s %5d %10s %5d" % (first_string, first_number, second_string, second_number))

# time = int(input("Введите время в секундах "))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")


# n = int(input("Введите число - "))
# total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
# print("Сумма чисел n + nn + nnn - %d" % total)

# profit = float(input("Введите выручку фирмы "))
# material_losses = float(input("Введите издержки фирмы "))
# if profit > material_losses:
#     print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / material_losses:.2f}")
#     workers = int(input("Введите количество сотрудников фирмы "))
#     print(f"Прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
# elif profit == material_losses:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")

# n = abs(int(input("Введите целое положительное число ")))
# max_number = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max_number:
#         max_number = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max)
#         break

# a = int(input("Введите результаты пробежки первого дня в км "))
# b = int(input("Введите общий желаемый результат в км "))
# result_days = 1
# result_km = a
# while result_km < b:
#     result_km *= 1.1
#     result_days += 1
# print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
