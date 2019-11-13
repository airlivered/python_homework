import re
print("Бондурянський Кирило Юрійович \nЛабораторна робота №2 \nВаріант 1 \nЗнаходження відповідної суми")
"""

Знаходження відповідної суми
"""
while True :
    def is_num(symbol):
        if re.match(r'^\-?\d+\.?\d+$', symbol):
            return True
    num = input('Введіть будь-яке дійсне число ')
    while not is_num(num):
        num = input("Введіть будь-яке дійсне число: ")

    def not_int(symbol):
        if re.search(r'[^(\d))]', symbol):
            return True
    high = input('Введіть верхню границю суми ')
    while not_int(high):
        high = input("Введіть верхню границю суми ")
    num = float(num)
    high = int(high)
    sum = 0
    for element in range(high + 1):
        sum = sum + element
        element += 1
    sum = sum*num
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

