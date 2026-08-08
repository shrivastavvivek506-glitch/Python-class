class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student:", self.name)


class BCAStudent(Student):
    def course(self):
        print("Course: BCA")


s = BCAStudent("Vivek")
s.show()
s.course()