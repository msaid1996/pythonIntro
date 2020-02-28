####vehicle exercise class
class Vehicle():
    # asks the user the speeds
    # modelInput = input("What is the model of your car?  ")
    # LimitInput = input("What is the speed limit of your car?  ")
    # speedInput = input("What is your acceleration speed in mph?  ")
    # brakeInput = input("What is your braking speed in mph?  ")
    # reverseInput = input("What is your new reverse speed?  ")

    def __init__(self, modelInput, speedInput, brakeInput, LimitInput, reverseInput):                  #asssigning all parameters in () to be used for below funct
        self.modelInput = modelInput
        self.speedInput = speedInput
        self.brakeInput = brakeInput
        self.LimitInput = LimitInput
        self.reverseInput = reverseInput

    def printModelCar(self, modelInput):
        return ("The model of your chosen car = " + modelInput)

    def printAllSpeeds(self, speedInput, brakeInput, reverseInput):
        a = print("Acceleration in mph = " + speedInput)
        b = print("Braking in mph = " + brakeInput)
        c = print("Reverse speed in mph = " + reverseInput)

    def speedLimitCheck(self, speedInput, brakeInput, LimitInput, reverseInput):
        if int(speedInput) > 0:                                                                                           #car will move, if not, car x move
            if int(speedInput) > int(LimitInput):                                                                           #car acceleration x be above vehicle speed limit = ERROR
                print("ERROR: Not Possible as acceleration shouldn't be over car speed limit")
                if int(brakeInput) > int(speedInput):
                    return ("ERROR: Not Possible")
                else:
                    return ("ERROR: Not Possible")
            else:
                print("Speed limit check is correct, car still MOVES")
                if int(reverseInput) == 0:                                                                              #checks if reverse speed is present, if not, proceed as normal
                    newSpeed = int(speedInput) - int(brakeInput)
                    print("Current speed in mph = " + str(newSpeed))
                    print("This is because: ")
                    if int(brakeInput) > int(speedInput):
                        return ("Brake speed is greater than acceleration speed, so vehicle STOPS. Current Speed = " + str(newSpeed))
                    else:
                        return ("Acceleration speed is greater than brake speed, so vehicle still MOVES. Current speed " + str(newSpeed) + "mph")

                if int(reverseInput) > 0:                                                                               #if a reverse speed is present, new reverse speed is taking into account as 'current speed'
                    newSpeed_reverse = int(reverseInput) - int(brakeInput)                                              #deceleration = -mph, slows down
                    print("Current speed  with reverse in mph = " + str(newSpeed_reverse))
                    print("This is because: ")
                    if int(brakeInput) > int(reverseInput):
                        return (
                            "Brake speed is greater than reverse speed, so vehicle decelerates at speed = " + str(newSpeed_reverse))
                    else:
                        return (
                            "Reverse speed is greater than brake speed, so vehicle still REVERSES at " + str(
                                newSpeed_reverse) + "mph")

        else:
            return ("Car does NOT MOVE, no acceleration added")


class Car(Vehicle):
    def __init__(self, modelInput, speedInput, brakeInput, LimitInput, reverseInput):                  #asssigning all parameters in () to be used for below funct
        self.modelInput = modelInput
        self.speedInput = speedInput
        self.brakeInput = brakeInput
        self.LimitInput = LimitInput
        self.reverseInput = reverseInput



# CAR child class
info = Car("volvo", "30", "20", "100", "5")
print(info.printModelCar("volvo"))
print(info.printAllSpeeds("30", "20","5"))
print(info.speedLimitCheck("30", "20", "100", "5"))
