class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"name: {self.name}")
        print(f"{self.name}'s age: {self.age}")

class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section
    
    def displayStudent(self):
        self.display()
        print(f"{self.name}'s section: {self.section}")

a = Student("coxy roxy", 3, "History")
a.displayStudent()