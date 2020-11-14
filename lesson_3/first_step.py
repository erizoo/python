var_1 = int(input("Введите делимое "))
var_2 = int(input("Введите делитель "))


def div(var_4, var_5):
    try:
        res = var_4 / var_5
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    return res


print(f'result  {div(var_1, var_2)}')
