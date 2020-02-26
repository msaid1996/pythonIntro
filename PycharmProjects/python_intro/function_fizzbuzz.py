#input user
#only numbers, if not change
#only min<max, if not change
#max limit of 50, if not change

def fizzbuzz(x,y):
    while x.isdigit() is False or y.isdigit() is False:
        print("Sorry, please insert a number")
        x = input("What is your start number?")
        y = input("What is your end number?")

    else:
        while int(x)>=50:
            print("Write NEW start number below 50")
            x=input("What is your NEW start number below 50?  ")
        while int(y) > 50:
            print("write a value below 50")
            y = input("What is your NEW end number that is below 50?")
        if int(x) < int(y):
            for num in range(int(x), int(y)):
                if num % 3 == 0 and num % 5 == 0:
                    print("FizzBuzz")
                elif num % 5 == 0:
                    print("Buzz")
                elif num % 3 == 0:
                    print("Fizz")
                else:
                    print(num)
        else:
            while int(x) > int(y):
                print("Insert a bigger end number")
                y = input("What is your BIGGER end number?")
            if int(x) < int(y):
                for num in range(int(x), int(y)):
                    if num % 3 == 0 and num % 5 == 0:
                        print("FizzBuzz")
                    elif num % 5 == 0:
                        print("Buzz")
                    elif num % 3 == 0:
                        print("Fizz")
                    else:
                        print(num)

    return y

x = input("What is your start number?")
y = input("What is your end number?")
print(fizzbuzz(x,y))

