n = int(input("vvedite cheslo"))

factorial = 1

for i in range(2, n + 1):
    factorial *= i

print(factorial)


#Факториалом числа n называется число 𝑛! = 1 ∙ 2 ∙ 3 ∙ … ∙ 𝑛.
# Создайте программу, которая вычисляет факториал
# введённого пользователем числа.