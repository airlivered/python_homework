print("Бондурянський Кирило Юрійович \nЛабораторна робота №1 \nВаріант 1 \nДруге завдання \nЗнайдення відповідного значення функції залежно від введеного числа")
def is_num(symbol1, symbol2, symbol3):
    if re.search(r'^\-?\d+\.?\d+$', symbol1):
        return True
    if re.search(r'^\-?\d+\.?\d+$', symbol2):
        return True
    if re.search(r'^\-?\d+\.?\d+$', symbol3):
        return True
x = input("Введіть перше число: ")
y = input("Введіть друге число: ")
z = input("Введіть третє число: ")
while not is_num(x, y, z):
    x = input("Введіть перше число: ")
    y = input("Введіть друге число: ")
    z = input("Введіть третє число: ")
x, y, z = float(x), float(y), float(z)
if x >= 0:
    print("Перше число більше або рівне 0, тому маємо " + str(x**2))
else: print("Перше число менше за 0, тому маємо " + str(x**4))
if y >= 0:
    print("Друге число більше за 0, тому маємо " + str(y**2))
else: print("Друге число менше за 0, тому маємо " + str(y**4))
if z >= 0:
    print("Третє число більше за 0, тому маємо " + str(z**2))
else: print("Третє число менше за 0, тому маємо " + str(z**4))
                                
