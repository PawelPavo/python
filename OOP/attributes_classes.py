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

print(my_dog.spots)
