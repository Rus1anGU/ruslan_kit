#Создайте список и введите его значения.
# Найдите наибольший и наименьший элемент списка, а также сумму и среднее арифметическое его значений.
import numpy
a = [2, 4, 8, 9, 10, 11, 15, 20, 23, 40]

a.append(41)
a.append(1)
add = 5
a.remove(11)
max_num = 0
for i in a:
    if i > max_num:
        max_num = i
print(max_num,"-maksemalnoe ceslo")


min_num = 1
for i in a:
    if i < min_num:
        min_num = i
print(min_num,"-minimalnoe ceslo")


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum(a),"-suma vsex chisel v spiske")

print(a)

print(numpy.mean(a),"-srednee arefmeticheskoe")




