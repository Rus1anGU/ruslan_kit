a = int(input('vvedi a'))
b = int(input('vvedi b'))

summ = 0
srednee = 0
if a < b:
    for i in range(a, b + 1):
        summ += i
        srednee += 1

print("sum = ", summ)
print("srednee =",summ / srednee)

#Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию,
# ввести необходимые числа и получить результат. Операции, которые необходимо реализовать:
# сложение, вычитание, умножение, деление, возведение в степень, синус, косинус и тангенс числа.

