from math import sin, cos, tan
print("ноль вместо знака завершит работу программы")
if s == "+":
  while True:
      try:
          first = float(input("first value"))
          second = float(input("second value"))
          print(first + second)
          break
      except ValueError:
          print("uesli ti ne lox write v stile float!")
elif sign == "-":
    first = float(input("first value"))
    second = float(input("second value"))



     s = input("знак (+,-,*,/): ")
     if s == '0':
        break
     if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("деление на ноль!")
     else:
        print("неверный знак операции!")