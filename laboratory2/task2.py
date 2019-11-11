import re
print("Бондурянський Кирило Юрійович \nЛабораторна робота №2 \nВаріант 2 \nЗнаходження найбільшої цифри числа")
def larNum(n):
    hList = list(str(n))
    i = 0
    while i < (len(hList) - 1):
        j = i + 1
        min_in = i
        while j < len(hList):
            if hList[j] < hList[min_in]:
                min_in = j
            j = j + 1
        temp = hList[i]
        hList[i] = hList[min_in]
        hList[min_in] = temp
        i = i + 1
    return hList[len(hList) - 1]
def is_int(symbol):
    if re.match(r'^\d+$', symbol):
        return True
while True:
    x = input('Введіть ціле число ')
    while not is_int(x):
        x = input("Введіть ціле число ")
    print("Найбільшою цифрою числа " + str(x) + " є " + larNum(x))
    while True:
        flag = input("Запустити програму знову? Введіть Так або Ні: ")
        if re.search(r'[^(Так|Ні)]', flag):
            print("Введені дані не задовільняють умовам")
            continue
        else:
            break
    if flag == 'Ні':
        break
    elif flag == 'Так':
        continue