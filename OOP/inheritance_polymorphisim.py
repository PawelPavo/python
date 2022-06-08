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
