class Cat():
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name #str
        self.age = age #number

    def meow(self):
        print('Hello, my name is {} and I am cat {}. I am {} years old.'.format(self.name, self.species, self.age))

my_cat= Cat('Gary',7)

print(my_cat.age)
print(my_cat.name)
print(my_cat.species)

my_cat.meow()
