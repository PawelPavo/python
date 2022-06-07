# PART 1

class Dog():
    def __init__(self,breed,name,spots, age):

        # Attributes
        # We take in the argument (param)
        # Assign it using self.attribute_name "self.attr_name = argument"
        self.breed = breed #str
        self.name = name #str
        self.spots = spots #bool True/False
        self.age = age #number
 

my_dog = Dog(breed='Lab',name='Gary',spots=False,age=7)

# You can pass the arguments without the name in order
my_dog_2 = Dog('Lab','Gary',False,7)

print(my_dog.spots)
print(my_dog_2.age)


# PART 2 ADDING CLASS OBJEST ATTRIBUTES - modifying above class

class DogTwo():
    # CLASS OBJECT ATTRIBUTES
    # SAME FOR ANY INSTANCE OF A CLASS - you dont use "self." here
    species = 'mammal'
    
    def __init__(self,breed,name,spots, age):
        self.breed = breed #str
        self.name = name #str
        self.spots = spots #bool True/False
        self.age = age #number


my_dog = DogTwo(breed='Lab',name='Gary',spots=False,age=7)

print(my_dog.species)


# PART 3 ADDING METHODS(aka OPERATIONS/Actions)- modifying above classe

class DogThree():
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed #str
        self.name = name #str

    # OPERATIONS/Actions ==> Methods
    def bark(self):
        print('WOOF! My name is {}'.format(self.name))

my_dog = DogThree('Lab','Joy')

my_dog.bark()
