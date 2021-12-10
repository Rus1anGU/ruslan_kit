class Ananas:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age

    def getSurname(self):
        return self.__age

    def __calcNumbers(self):
        return "some store..."+ str(self.__age ** 2)

    def getCalculation(self):
        self.__calcNumbers()
        return "skoro novu got"+ str(31-7)

    def getDays(self):
        return  self.__calcDays()

    CURRENTMANTH = 12
    CURRENTDATE = 7

@staticmetod
def __calcDays():
    return "days befor novu got" + str(31-7)
def gatDays(self):
    return

myobj = Apple("SpangeBob,Patrik", 30)
print(Ananas.name, Ananas._surname,Ananas.__age)
print(myobj.name, myobj._surname, myobj._Ananas__age)
print(myobj.getSurname())
print(myobj.getDays())
print