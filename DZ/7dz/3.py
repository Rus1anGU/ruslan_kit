#Простым называется число, которое делится нацело только на единицу и само себя. Число 1 не считается простым.
# Напишите программу, которая находит все простые числа в заданном промежутке, выводит их на экран,
# а затем по требованию пользователя выводит их сумму либо произведение.


diapazonn = int(input("Введите начало диапазона для поиска простых чисел: "))
diapazonk = int(input("Введите конец диапазона для поиска простых чисел: "))
for num in range(diapazonn, diapazonk):
    count = 0
    delitel = 2
    while delitel < num:
        if num % delitel == 0:
            count += 1
        delitel += 1
    if count == 0:
      print({num})

