count = int(input("VVEDI dlinu storon: "))
print("* " * count)
for _ in range(count - 2):
    print("* ", "  " * (count - 3), "* ")
print("* " * count)


# Создайте программу, которая рисует на экране
# прямоугольник из звёздочек заданной
# пользователем ширины и высоты.