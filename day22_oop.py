class student:
    pass
student1=student()
student1.name="Ganesh"
student1.age=25
print(student1.name)
print(student1.age)


class student:
    def greet(self):
        print("Hello")

student1=student()
student1.greet()


class student:
    def greet(self):
        print("Hello,I am",self.name)

student1=student()
student1.name="Ganesh"
student1.greet()


#the init method

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
student1=student("Ganesh",25)
print(student1.name)
print(student1.age)


#creating multiple objects

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
student1=student("Ganesh",25)
student2=student("Isha",23)
print(student1.name,student1.age)
print(student2.name,student2.age)
