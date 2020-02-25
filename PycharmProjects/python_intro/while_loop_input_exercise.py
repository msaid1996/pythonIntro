#-------------------------LONGER CODE THAN PAV'S pav_whileloopEx file
min=input("What is your min. number?  ")
max=input("What is your max. number?  ")

while min.isnumeric()==True and max.isnumeric()==True:
    if int(min)<int(max):
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
        if int(min)<int(max):
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
        if int(min)<int(max):
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
        if int(min)<int(max):
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
