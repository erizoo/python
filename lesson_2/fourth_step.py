str_input = str(input("Введите строку из нескольких слов, разделённых пробелами "))
str_list = str_input.split(" ")
for idx, item_str in enumerate(str_list):
    if len(item_str) > 10:
        print(f"{idx + 1}) {item_str[0:10]} ...")
    else:
        print(f"{idx + 1}) {item_str}")


