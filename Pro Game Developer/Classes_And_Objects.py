class Person:
    count = 0 # #class variable

    def __init__(self, name, age):
        self.name = name # instance variable
        self.age = age
        Person.count += 1

    def greet(self):
        print("Hello, my name is " + self.name)

Person1 = Person("Jediael", 11)
Person2 = Person("David", 11)
Person3 = Person("Mia", 10)
print(Person.count)
Person1.greet()