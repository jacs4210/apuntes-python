class Mammal:
    def speak(self):
        print("Some sound")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("Vroom")


cat1 = Cat()
cat1.be_annoying()

dog1 = Dog()
dog1.speak()
