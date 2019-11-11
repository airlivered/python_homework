import re
print("Бондурянський Кирило Юрійович \nЛабораторна робота №2 \nВаріант 1 \nЗнаходження відповідної суми")
while True :
    def is_num(symbol):
        if re.match(r'^\-?\d+\.?\d+$', symbol):
            return True
    x = input('Введіть будь-яке дійсне число ')
    while not is_num(x):
        x = input("Введіть будь-яке дійсне число: ")

    def not_int(symbol):
        if re.search(r'[^(\d))]', symbol):
            return True
    n = input('Введіть верхню границю суми ')
    while not_int(n):
        n = input("Введіть верхню границю суми ")
    x = float(x)
    n = int(n)
    sum = 0
    for i in range(n + 1):
        sum = sum + i
        i += 1
    sum = sum*x
    print("Значення суми рівне " + str(sum))
    while True:
        flag = input("Запустити програму знову? Введіть Так або Ні: ")
        if re.search(r'[^(Так|Ні)]', flag):
            print("Введені дані не задовільняють умовам")
            continue
        else: break
    if flag == 'Ні':
        break
    elif flag == 'Так':
        continue

