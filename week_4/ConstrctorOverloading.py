class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
# Example Usage
person1 = Person("shiny")
person2 = Person("srinith", 8)
# Output
print(person1.name, person1.age)
print(person2.name, person2.age)