class Animal:
    def __init__(self, name, rost, ves, age):
        self.name = name
        self.rost = rost
        self.ves = ves
        self.age = age

    def run(self, speed):
      print("animal hes speed", speed)

    def voice(self):
      print("ghj")


class Dog(Animal):
    def voice(self):
      print("gafff")

    def swim(self):
      print(self.name + "i can swim")

class Cat(Animal):
    def voice(self):
      print("mey-sey")

    def lazit(self):
      print(self.name +"i can to lazit")

class Cow(Animal):
    def voice(self):
      print("syyyy")

    def milk(self):
      print(self.name +"come to me")




dog1 = Dog("sharik",70 ,35, 3)
cat1 = Cat("Murzik",20, 5, 2)
cow1 = Cow("Milka", 90 ,60, 2)


dog1.swim()
dog1.voice()
dog1.run(20)

cat1.swim()
cat1.voice()
cat1.run(25)

cow1.swim()
cow1.voice()
cow1.run(3)


