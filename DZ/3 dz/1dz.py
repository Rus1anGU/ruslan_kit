imena = ['oleg', 'vlad', 'jojo']
while True:
    name = (input("Attention! Vvedite vashe ima?: ")).split()[-1]
    if name in imena:
        print("f'da mou gospodin!, {name}!'")
    else:
        print('pliz uxodi')


#Напишите программу, которая спрашивает у пользователя его имя,
# и если оно совпадает с вашим, выдаёт определённое сообщение.
