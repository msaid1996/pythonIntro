####vehicle exercise class

class Car():
    def __init__(self, model, accSpeed, brakeSpeed, carLimit, reverseSpeed):                  #asssigning all parameters in () to be used for below funct
        self.model = model
        self.accSpeed = accSpeed
        self.brakeSpeed = brakeSpeed
        self.carLimit = carLimit
        self.reverseSpeed = reverseSpeed


    def printModelCar(self, model):
        print("The model of your chosen car = " + model)

    def printAllSpeeds(self, accSpeed, brakeSpeed, reverseSpeed):
        a = print("Acceleration in mph = " + accSpeed)
        b = print("Braking in mph = " + brakeSpeed)
        c = print("Reverse speed in mph = " + reverseSpeed)

    def speedLimitCheck(self, accSpeed, brakeSpeed, carLimit, reverseSpeed):
        if int(accSpeed) > 0:                                                                                           #car will move, if not, car x move
            if int(accSpeed) > int(carLimit):                                                                           #car acceleration x be above vehicle speed limit = ERROR
                print("ERROR: Not Possible as acceleration shouldn't be over car speed limit")
                if int(brakeSpeed) > int(accSpeed):
                    print("ERROR: Not Possible")
                else:
                    print("ERROR: Not Possible")
            else:
                print("Speed limit check is correct, car still MOVES")
                if int(reverseSpeed) == 0:                                                                              #checks if reverse speed is present, if not, proceed as normal
                    newSpeed = int(accSpeed) - int(brakeSpeed)
                    print("Current speed in mph = " + str(newSpeed))
                    print("This is because: ")
                    if int(brakeSpeed) > int(accSpeed):
                        print("Brake speed is greater than acceleration speed, so vehicle STOPS. Current Speed = " + str(newSpeed))
                    else:
                        print("Acceleration speed is greater than brake speed, so vehicle still MOVES. Current speed " + str(newSpeed) + "mph")

                if int(reverseSpeed) > 0:                                                                               #if a reverse speed is present, new reverse speed is taking into account as 'current speed'
                    newSpeed_reverse = int(reverseSpeed) - int(brakeSpeed)                                              #deceleration = -mph, slows down
                    print("Current speed  with reverse in mph = " + str(newSpeed_reverse))
                    print("This is because: ")
                    if int(brakeSpeed) > int(reverseSpeed):
                        print(
                            "Brake speed is greater than reverse speed, so vehicle decelerates at speed = " + str(newSpeed_reverse))
                    else:
                        print(
                            "Reverse speed is greater than brake speed, so vehicle still REVERSES at " + str(
                                newSpeed_reverse) + "mph")

        else:
            print("Car does NOT MOVE, no acceleration added")


# asks the user the speeds
modelInput = input("What is the model of your car?  ")
LimitInput = input("What is the speed limit of your car?  ")
speedInput = input("What is your acceleration speed in mph?  ")
brakeInput = input("What is your braking speed in mph?  ")
reverseInput = input("What is your new reverse speed?  ")

#assign to call
info = Car(modelInput, speedInput, brakeInput, LimitInput, reverseInput)                  #all assign inputs above added in parameters ()

#prints the model of car
print(info.printModelCar(modelInput))

#prints the speed
print(info.printAllSpeeds(speedInput, brakeInput, reverseInput))

#checks the car vehicle speed limit against acc speed & new speed limit & car move/stationary
print(info.speedLimitCheck(speedInput, brakeInput, LimitInput, reverseInput))


#call the stuff in the speedlimitcheck








#####################################################################

#checks whether vehicle can move or not in BrakeMoreAcc funct
#print(info.BrakeMoreAcc(speedInput, brakeInput))

# def BrakeMoreAcc(self, accSpeed, brakeSpeed):
#     if int(brakeSpeed) > int(accSpeed):
#         print("Brake speed is greater than acceleration speed, so vehicle STOPS")
#     else:
#         print("Acceleration speed is greater than brake speed, so vehicle still MOVES")
#
