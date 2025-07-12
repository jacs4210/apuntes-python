class Person:
    def __init__(self, name="", last_name=""):
        self.name = name
        self.last_name = last_name

    def get_name(self):
        print("get_name")

person1 = Person()
person1.name = "Jairo"
person1.last_name = "Cuartas"
print(f"Hi, {person1.name} {person1.last_name}")

person2 = Person("John", "Doe")
print(f"Hi, {person2.name} {person2.last_name}")