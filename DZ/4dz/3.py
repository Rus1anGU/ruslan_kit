L = 10

rows = int(input ( 'Enter a number of rows: ' ) )

height = rows

inner_buffer = [0, 1, 3]
while len(inner_buffer) <= rows:
    inner_buffer.append(inner_buffer[-1]+2)

while height > 0:
    outer_padding = ' '*(rows - height)
    if height == 1:
        print(outer_padding + '*')
    else:
        inner_padding = ' '*(inner_buffer.pop()-2)
        print(outer_padding + '*' + inner_padding + '*')
    height = height - 1

#Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print()
# выведите на экран прямоугольный треугольник.