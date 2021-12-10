#Создайте две функции, вычисляющие значения определённых
# алгебраических выражений. Выведите на экран таблицу
# значений этих функций от -5 до 5 с шагом 0.5.

def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3
    print(x)


def main():
    for i in range(-5, 5, 0.5):
        y = function(i)
        print('function(', i, ') =', y, sep='')


main()
