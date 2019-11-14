from WordReplace import separator, finder, is_that_many, swapper, counter, validators
"""

Аргументом є речення. Поміняти місцями два слова з найбільшою і найменшою довжиною, за
умови що вони єдині.
Оскільки єдиність даних слів є параметром, що можна змінити, програма враховує два випадки:
1)Вони єдині, зміна відбувається автоматично
2)Вони не єдині, в даному випадку маємо безліч можливих варіантів зміни порядку, тому дамо
користовачу самому вирішити, що поміняти із чим
"""
def swap_all(sentence, sep_character, needed_for_maximum, needed_for_minimum):
    """

    :param sentence: str(), зміна порядку, сукупність будь-яких символів, killer queen
    :param sep_character: str(), нічого, один символ, _
    :param needed_for_maximum: int(),
    :param needed_for_minimum:
    :return:
    """

    """
    
    Створюємо список із слів(розділяючий символ задається на місці аргументу sep_character).
    """
    words = separator.separate(sentence, sep_character)

    """ 
    
    Створюємо список із довжин слів. 
    """
    lengths = counter.count(words)

    """
    
    Створюємо список з індексів максимальних та мінімальних елементів. Нам це необхіно для
    випадку, коли слова з відповідною довжиною не єдині
    """
    max_indeces, min_indeces = finder.max_min_index(lengths, "max"), finder.max_min_index(lengths, "min")
    print(max_indeces, min_indeces)

    """
    
    Перевіряємо, чи вони відповідють заданій умові
    """

    if not (is_that_many.check(needed_for_maximum, len(max_indeces)) and is_that_many.check(needed_for_minimum, len(min_indeces))):
        print("Starting conditions were not satisfied")
        quit()

    """
    
    Перевіряємо, чи вони єдині
    """
    if needed_for_maximum == 1 and needed_for_minimum == 1:
        words = swapper.swap(words, max_indeces[0], min_indeces[0])
    else: swapper.multi_swap(max_indeces, min_indeces, words)
    """
    
    З'єднуємо у один рядок
    """
    sentence = sep_character.join(words)
    return sentence

if __name__=='__main__':
    sentence = input("Введіть речення: ")

    sep_character = input("Введіть роздільні символи: ")

    needed_for_maximum = input("Введіть необхідне число максимальних елементів: ")

    while not validators.is_int(needed_for_maximum):
        needed_for_maximum = input("Введіть необхідне число максимальних елементів: ")
    needed_for_minimum = input("Введіть необхідне число мінімальних елементів: ")

    while not validators.is_int(needed_for_minimum):
        needed_for_minimum = input("Введіть необхідне число мінімальних елементів: ")

    print(swap_all(sentence, sep_character, int(needed_for_maximum), int(needed_for_minimum)))

