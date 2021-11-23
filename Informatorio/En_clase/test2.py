
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier('Miles',4)
buddy = Dachshund('Buddy',9)
jack = Bulldog('Jack',3)
jim = Bulldog('Jim',5)

print(isinstance(miles,Dog))

print(isinstance(jack,Dachshund))

print(isinstance(miles,Bulldog))

print(isinstance(jack,Dog))


class Dog:
    def walk(self):
        return "*walking*"

    def speak(self):
        return "Woof!"

class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"

bobo = JackRussellTerrier()
print(bobo.speak())

class test:
    def __init__(self) -> None:
        self.variable = "OLD"
        self.Change(self.variable)

    def Change(self,var):
        var = "NEW"

obj = test()

print(obj.variable)