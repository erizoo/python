goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input(" Для выхода нажмите 'Q', для продолжения нажмите 'Enter', для анализа нажмите 'A' ").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Анализ данных \n\n')
        for key, value in analytics.items():
            print(f' {key}: {value}')
    for f in features.keys():
        feature_ = input(f'\n Введите данные "{f}" ')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
