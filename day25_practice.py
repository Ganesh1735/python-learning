class Student:
    def __init__(self):
        self.__marks=80
    def show_marks(self):
        print("Marks",self.__marks)    

marks=Student()
marks.show_marks()