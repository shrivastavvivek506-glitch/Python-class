# class Calc:
#     def add(self, a, b=0):
#         print(a + b)

#         c = Calc()
#         c.add(5)
#         c.add(5, 10)

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks") 

d = Dog()
d.sound()                
