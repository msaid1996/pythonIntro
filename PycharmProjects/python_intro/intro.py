# is a comment, 2 spaces after a code
print('hello world!')

# string
hi = 'hello world!'  # string
name = 'kaka'
print(hi)
print(hi + ' ' + name)

# number
x = 1  # int
y = 2  # int
z = 3.5  # float
d = x + y
print(d)

# int & string cannot be together

# -------------------METHODS - alters something about the variables
## E.g. print

# -------------------TYPE() - let us find the type of object: class & int/string/float etc
# x print, it returns instead
type(hi)  # only returns
print(type(hi))  # prints string type

print(type(z))  #prints float type

print(type(type)) #prints type

print('xxxxxxxx')
#----------------------------user input prompt
hi='hello'
name=input('What is your name?  ')
print(hi + ' ' +name)
#ex: name, age, fav snacks
find_name=input('What is your name?  ')
find_age=input('What is your age?  ')
find_snack=input('what is your favourite snack?  ')
answer = 'Your name is' + ' ' + find_name + ',' + ' ' + 'Your age is' + ' ' + find_age + ',' + ' '+ 'Your fav snack is' + ' ' + find_snack
print(answer)

diffAnsw = 'this is your name, age, fav snack respectively: %s %s %s' %(find_name, find_age, find_snack)
print(diffAnsw)

#-------------------------------------------int/float/complex
#int = whole no
#float = decimal numbers
#complex = x + yi -> real and imaginary numbers
print('------------------')


x=2
y=3
z = complex(x,y)
print(z)
print(z.real)  #returns real part
print(z.imag)  #returns imaginary part

f = 1.5
print(x+f) ##= int + float = returns a float
print(x*f) ##= int * float = returns a float
print(x/f) ##= int / float = returns a float

print(x+y) ##= int + int = returns a int
print(x*y) ##= int * int = returns a int
print(x/y) ##= int / int = returns a flaot

#------------------------------------------------quotes
print('------------------')

single = 'can use \'hello\''
singles = 'can use "hello"'
print(single)
print(singles)

double = "can use this"
print(double)

#------------------------------------------------slice : to find index/position of charac in string
print('------------------')

hi = 'helloworld'
print(hi[1]) #returns e
print(hi[1:]) #returns after e = ello world
print(hi[1:4]) #returns position 1 - 3 = ell
print(hi[-2:]) #returns after ld
print(hi[::2]) #returns 1st & returns every 2 charac
print(hi[::-1]) #returns opposite word
print(hi[::-5]) #returns 1st & returns opposite word

#---------------------------------------------------STRIP strip()
print('------------------')

hi = '      Hello World             '
print(hi)
#length character?
print(len(hi))                              #includes space
#remove whitespace - strip()
hi=hi.strip()                               #Updating hi variable & strip empty spaces before & after string, x middle of string
print(hi)
print(len(hi))                              #includes space
#----------------------------------------------------FUNCTIONS
print('------------------')

new = 'pineapple is my favourite'
#count
print(new.count('p'))   # counts the 'p' in variable
print(new.upper())      #uppercase
print(new.lower())      #lowercase
print(new.capitalize())                     #uppercase the first char ONLY in string
print(new.replace('pineapple', 'banana'))   #replaces pineapple into banana in variable

#------------------------------------FUNCTIONS 2
print('------------------')

hi = 'Hello World'

print(hi.isalpha())                 #check true = if all string is alphabetically, false= includes space, punctuations
print(hi.islower())
print(hi.endswith('world'))
print(hi.startswith('Hello'))


#----------------------------------------------------------CONVERT DATA TYPES
print('------------------')

a='50'
print(type(a))
a=int(a)
print(type(a))

a='50.8244545'
print(type(a))
a=float(a)
print(type(a))

#----------------------------------------------------BOOLEAN: True/False
print('------------------')

a = True
b = False

print(a==b)     #false
print(a!=b)     #true
print(a>=True)  #true
print(a<=False) #false
print(a>b)      #true
print(a<b)      #false
print('------------------')

x=0
y=10
z=-1
m=None              # = NULL & is not true = false
print(bool(x))      #returns false (0=FALSE)
print(bool(y))      #returns true (NOT 0 = TRUE)
print(bool(z))      #returns true (NOT 0 = TRUE)
print(bool(m))      #returns true (NULL = not true = FALSE)

#------------------------------------------tuples
#similar to list - but items in list x be modified
shopping_list = ["nutella", "oranges", "mickie's of scotland", "tofu", "bourbon biscuits"]
print(shopping_list)



