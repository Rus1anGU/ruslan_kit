def func(x):
    if -5<=x<=5:
        return x*x
    elif x < -5:
        return 2*abs(x)-1
    else:
        return 2*x

for i in range(-10,11):
    print(func(i), end=' ')
print()


#Напишите программу, которая вычисляет значение функции в
# диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
#y = x2 при -5 <= x <= 5;
#y = 2*|x|-1 при x < -5;
#y = 2x при x > 5.
#Вычисление значения функции оформить в виде программной функции, которая
# принимает значение x, а возвращает полученное значение функции (y).