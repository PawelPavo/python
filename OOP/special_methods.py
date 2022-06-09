# Special methods AKA magic or Dunder


class Book():
    def __init__(self, title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    # __str__ is a special method that return string representation
    # if someone wants to print the Book class
    
    def __str__(self):
        return f"{self.title} by {self.author} {self.pages}"

    # lenght special method

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


b=Book('Python','Jose',200)

print(b)

print(len(b))


# You can delere 'b' from the computer memory
# del workouts without __del__ but we can customize it by using __del__
del b

