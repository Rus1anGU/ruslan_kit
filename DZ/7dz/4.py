#Создайте список, введите количество его элементов и сами значения, выведите эти значения на экран в обратном порядке.

a = [2, 4, 8, 9, 10, 11, 15, 20, 23, 40]
for i in reversed(a):
    print(i, end=',')
