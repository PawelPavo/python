
# PASSING A FUNCTION AS AN ARGUMENT
def hello():
    return 'Hi Pawel!'



def other(some_function):
    print('Other code runs here.')
    # Here we print() function because it has a 'str' return
    print(some_function())

# Passing the function hello() but not executing it - "RAW" function
other(hello)

print('========== BREAK ==========')

# CONSTRUCTING DECORATOR

def new_decorator(original_func):
    
    def wrap_func():

        print('Some extra code, BEFORE the original function.')

        original_func()

        print('Some extra code AFTER the original function.')

    return wrap_func


def func_needs_decorator():
    print('I want to be decorated')

# Regular execution
func_needs_decorator()

# Decorated execution:
# Assign the function to the decorator func with func that wants the decorator as an argument
decorated_func=new_decorator(func_needs_decorator)
decorated_func()

print('========== BREAK ==========')

# DECORATOR SYTAX for above
@new_decorator
def func_needs_decorator_too():
    print('I want to be decorated too')

func_needs_decorator_too()




