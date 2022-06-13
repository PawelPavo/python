class Cat():
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name #str
        self.age = age #number

    def meow(self):
        print('Hello, my name is {} and I am cat {}. I am {} years old.'.format(self.name, self.species, self.age))

    # YOU CAN PASS OUTSIDE ARGS TO THE Methods

    def meow_two(self, number):
        print('Hello, this is {} the cat again. The year is {}.'.format(self.name, number))
    

my_cat= Cat('Gary',7)

print(my_cat.age)
print(my_cat.name)
print(my_cat.species)

my_cat.meow()

# YOU CAN PASS OUTSIDE ARGS TO THE "meow" Methods - need to include it in the method 'meow_two'
my_cat.meow_two(2022)


class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1): # we gave radious default value just in case nothing is passed
        self.radius=radius
        self.area = radius*radius*self.pi #self.area = radius*radius*Circle.pi - ONLY FOR CLASS OBJECT DIRECT ATTR
    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2 # self.radius * Circle.pi * 2 

my_circle = Circle()
print(my_circle.get_circumference())
print(my_circle.area)
# Pass the value when you create an instance of the circle DIFFRENT from passing it direct to the method
my_custom_circle = Circle(30)
print(my_custom_circle.area)
print(my_custom_circle.get_circumference())



  
