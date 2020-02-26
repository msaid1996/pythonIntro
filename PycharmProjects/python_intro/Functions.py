# DEF - prevents repeated code being written
# use RETURN, x PRINT() when using def function

print("----------------------------SINGLE ARGUMENT--------------------------")


def useless_print(a):  # a = argument
    print(a)

useless_print("hello")

print("----------------------------MULTIPLE ARGUMENTS--------------------------")


def useless_print(num1, num2):
    return (num1 + num2)

print(useless_print(1, 2))

print("*******")

def multi(*a):                          # * = allows multiple arguments to take place
    print(type(a))                      # checks the type of argument = tuple = x changeable list w. ()
    for args in a:                      #iterates each argument and prints them
        print(args)
        
multi("hello", 4, 54677)

print("----------------------------DEFAULTS ARGUMENTS--------------------------")
#useful for data analytics - many arguments are default/essential/non-essential


def useless_print(num1 = 1, num2 = 2):
    return (num1 + num2)

print(useless_print())

print("*******")

def useless_print(num1 = 1, num2 = 2):
    return (num1 + num2)

print(useless_print(5,8))                   #overrides the default argument in def


