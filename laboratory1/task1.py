print("Бондурянський Кирило Юрійович \nЛабораторна робота №1 \nВаріант 1 \nПерше завдання \nПереведення кута з радіанної міри в градусну")

"""
Переведення кута з радіанної міри в градусну
"""

def is_num(symbol):
    if re.search(r'^\-?\d+\.?\d+$', symbol):
        return True
angle = input("Введіть кут радіанної міри: ")
while not is_num(angle):
    angle = input("Введіть кут радіанної міри: ")
angle = float(angle)
float_deg_angle = angle*57.29577
deg = int(float_deg_angle)
min = int((float_deg_angle - deg)*60)
sec = int(((float_deg_angle - deg)*60 - min)*60)
print("Кут " + str(angle) + " радіан рівний " + str(deg) + " градусам " + str(min) + " хвилинам і " + str(sec) +" секундам")
