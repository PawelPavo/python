# INHERITANCE

class Animal():
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')



class Dog(Animal):   # Passing 'Animal' class to inherit the props\
    def __init__(self):
        Animal.__init__(self)
        print('Dog created!')

    def bark(self):
        print('WOOF!')

myanimal=Animal()
myanimal.eat()
mydog=Dog()
mydog.eat()
mydog.bark()
#https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478298?start=15#questions

# POLYMORPHYSIM


class Dog2():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name + " says woof!"


class Cat2():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name + " says meow!"


niko=Dog2('Niko')
felix=Cat2('Felix')

print(niko.speak())

print(felix.speak())


for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)

pet_speak(felix)



class Animal2():
    def __init__(self,name):
        self.name = name

    def speak(self):
        # this will throw an error because we dont the ANIMAL class to be used directly
        raise NotImplementedError("Subclass must implement this subclass method")

# Must use an instance of the "Animal" and then redefin the "speak" subclass as you need it, many times
# (poly morph the class to something you need) 

class Dog3(Animal2):

    def speak(self):
        return self.name + " says WOOF! 3"

class Cat3(Animal2):
    
    def speak(self):
        return self.name + " says meow! 3"


filo=Cat3("Filo")

lilo=Dog3("Lilo")

print(filo.speak())
print(lilo.speak())













    
    
