# classes = template w. shared attributes
print("--------------------------------DEFINING THE CLASS-----------------------------------")


class Dog:
    animal_kind = 'canine'  # class variable = 'attributes'

    def bark(self):  # class method = "doing thing" - defining them
        print(self.animal_kind)  # like a def funct but with class = called a class method
        return "woof"


print("**** check ****")
print(Dog)  # prints <class '__main__.Dog'>      where the class Dog comes from
print(Dog.animal_kind)  # prints canine                      Prints the class variable
print(Dog.bark(Dog))  # prints woof      return

print("**** assign name of dog ****")
fido = Dog()
pido = Dog()

print("**** check ****")
print(type(fido))
print(type(pido))
print(pido.animal_kind)  # canine

print("**** convert the animal kind from dog to cat ****")
fido.animal_kind = "cat"  # fido is applied, now cat
print(pido.animal_kind)  # still canine
print(fido.animal_kind)  # only fido is cat

print("**** convert the animal kind to cat ****")
Dog.animal_kind = "parrot"  # class Dog is applied to be 'parrot'
print(pido.animal_kind)  # applied - x applied before = 'parrot'
print(fido.animal_kind)  # x applied - already changed before. Otherwise if not applied before --> will be 'parrot' too!

print("--------------------------------INSTANTIATING THE CLASS-----------------------------------")


# Instantiation = making an instant
# inititalisation = def __init__(self):

class Dog:
    animal_kind = 'canine'  # class variable

    def __init__(self, name, colour):  # initialisation!**************
        self.name = name
        self.colour = colour

    def bark(self):  # class method
        print(self.animal_kind)
        return "woof"


print("**** assign name of dog ****")
fido = Dog("Fido", "green")
pido = Dog("pido", "red")

print("**** print ****")
print(fido.name)
print(fido.colour)

print("--------------------------------INSTANTIATING THE CLASS exercise-----------------------------------")


# Instantiation = making an instant
# inititalisation = def __init__(self):

class Elephant:
    animal_kind = 'Sumatran'  # class variable
    animal_country = 'India'  # class variable
    animal_tusk = 'Pointy'  # class variable

    def __init__(self, name, colour, age, trunk_length):  # define them before initialisation
        self.name = name
        self.colour = colour
        self.age = age
        self.trunk_length = trunk_length

    def noise(self):                                       # class method - applies to each init
        print(self.animal_kind)
        return "ooooooooooo"

print("**** assign name of dog ****")
Ella = Elephant("Ella", "Dark Grey", 21, 2)
Simmi = Elephant("Simmi", "Light Grey", 5, 0.2)
Neno = Elephant("Neno", "White", 50, 3)

print("**** print ****")
print(Ella.name)
print(Simmi.colour)
print(Elephant.noise(Elephant))  # prints woof

print("------------------------------4 PILLARS OF OBJECT ORIENTTATED PROGRAMMING-----------------------------------")

print("2. Inheritance e.g.")
class Animal:
    def __init__(self):                         #intitialisation -- every animal is alive 'I'm here'
        self.alive="I'm here"

    #def __init__(self, alive):                 # intitialisation -- every animal is EITHER alive OR NOT
     #   self.alive = alive

    def breathe(self):                           #class method
        print("I breathe")

    def moves(self):                             #class method
        print("I move")


class Reptile(Animal):                          # INHERITANCE HERE! --> put class 'Animal' to this class 'Reptile' = reptile is inherited from animal
    def __init__(self):                         #gain access to ALL METHODS IN *parent* class - can use: init ALIVE, BREATHER, MOVES
        super().__init__()

    def cold(self):                             #own unique method/function
        print("I'm cold blooded")

#assign
print("**************Parent child:")

jean = Animal()         #jean is an animal
print(jean.alive)
print(jean.breathe())

print("**************Class child:")


ali = Reptile()         #Ali is a reptile
print(ali.cold())       #from CHILD
print(ali.alive)        #from PARENT ******************
print(ali.breathe())    #from PARENT ******************
print(ali.moves())      #from PARENT ******************

print("3. Encapsulation e.g.")


