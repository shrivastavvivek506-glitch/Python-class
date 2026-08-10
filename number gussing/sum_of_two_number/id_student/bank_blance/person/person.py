class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        class student(Person):  # Inheritance
            s1 = Person("Vivek", 19)
            s1.show() 
    