class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):   # Inheritance
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)   # Parent constructor call
        self.roll_no = roll_no

    def display(self):
        self.show()
        print("Roll No:", self.roll_no)


# Object
s1 = Student("Vivek", 19, 99)
s1.display()