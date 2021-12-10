# Напишите рекурсивную функцию, которая вычисляет сумму натуральных чисел, которые входят в заданный промежуток.

def recur_sum(n):

    if n <= 1:
        return n
    else:
        return n + recur_sum(n - 1)


num = int("123")

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is ", recur_sum(num))