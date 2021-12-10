# Создайте программу, которая состоит из функции, которая принимает
# три числа и возвращает их среднее арифметическое, и главного цикла,
# спрашивающего у пользователя числа и вычисляющего их средние значения
# при помощи созданной функции.
cheslo_a = int(input("vvedi pervoe"))
cheslo_b = int(input("vvedi vtoroe"))
cheslo_c = int(input("vvedi tretie"))
import numpy
listnumbers = (cheslo_a, cheslo_b, cheslo_c)
print ("The mean is =",numpy.mean(listnumbers))
