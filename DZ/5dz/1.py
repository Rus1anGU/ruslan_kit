# Создайте функцию, которая выводит приветствие для пользователя
# с заданным именем. Если имя не указано, она должна выводить
# приветствие для пользователя с Вашим именем.

def whoAreYouAndHello():
    y = True
    x = input()
    while y != False:
        if x.upper():
            x = input()
        if x.isalpha() and x.upper() and x.lower():
            y = False
        else:
            x = input()
    print('Привет, ', x, '!', sep='')
whoAreYouAndHello()