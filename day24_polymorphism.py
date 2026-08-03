class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")
        
dog=Dog()
cat=Cat()
cow=Cow()

animal_list = [dog, cat, cow]
for animal in animal_list:
    animal.sound()