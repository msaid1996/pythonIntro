x=1
while x<10:
    print(x)                    #continuosly prints 1 if this is the only code
    x+=1                        #adds 1 until it reaches 9 (<10)

y=1
while y<10:
    print("it's working" + str(x))                    #continuosly prints 1 if this is the only code
    y+=1

z=1
while z<10:
    print(f"it's working {x}")                    #continuosly prints 1 if this is the only code
    z+=1

m=1
while m<10:
    print(f"it's working {x}")                    #continuosly prints 1 if this is the only code
    m+=1
    if m ==4:
        break
print("-----------------------")

min=input("What is your min. number?  ")
max=input("What is your max. number?  ")

while min.isnumeric()==True and max.isnumeric()==True:
    if min<max:
        for x in range(int(min), int(max)):
            if x % 3 == 0 and x % 5 == 0:
                print("fizzbuzz")
            if x % 3 == 0:
                print("fizz")
            if x % 5 == 0:
                print("buzz")
            else:
                print(x)
    break

while min.isnumeric()==False and max.isnumeric()==False:
    print("please put in a number in min number")
    min = input("What is your min. number?  ")
    print("please put in a number in max number")
    max = input("What is your max. number?  ")
    if min.isnumeric() == True and min.isnumeric() == False:
        if min < max:
            for x in range(int(min), int(max)):
                if x % 3 == 0 and x % 5 == 0:
                    print("fizzbuzz")
                elif x % 3 == 0:
                    print("fizz")
                elif x % 5 == 0:
                    print("buzz")
                else:
                    print(x)
        break

while min.isnumeric()==False:
    print("please put in a number")
    min = input("What is your min. number?  ")
    if min.isnumeric() == True:
        if min < max:
            for x in range(int(min), int(max)):
                if x % 3 == 0 and x % 5 == 0:
                    print("fizzbuzz")
                elif x % 3 == 0:
                    print("fizz")
                elif x % 5 == 0:
                    print("buzz")
                else:
                    print(x)
        break

while max.isnumeric()==False:
    print("please put in a number")
    max = input("What is your max. number?  ")
    if max.isnumeric() == True:
        if min < max:
            for x in range(int(min), int(max)):
                if x % 3 == 0 and x % 5 == 0:
                    print("fizzbuzz")
                elif x % 3 == 0:
                    print("fizz")
                elif x % 5 == 0:
                    print("buzz")
                else:
                    print(x)
        break
