
# Make the Drone blueprint
class Drone:

    # Constructor for initializing a new object
    
    def __init__(self):
        self.__speed = 0.0
        self.__height = 0.0
    
    #class method to increase speed
    def accelerate(self):
        if self.__speed < 40:
            self.__speed += 5
        else:
            print("Drone has reached maximum forward speed")


    #class method to decrease speed
    def decelerate(self):
        if self.__speed > -40:
            self.__speed -= 5
        else:
            print("Drone has reached maximum reverse speed")


    #class method to increase height
    def ascend(self):
        if self.__height <= 5000:
            self.__height += 20
        else:
            print("Drone can not fly any higher")

    # class method to decrease height
    def descend(self):
        if self.__height == 0:
            print("drone can not fly any lower")
        else:
            self.__height -= 20

    def __str__(self):
        print("Speed:", self.__speed, " mph")
        print("Height:", self.__height, " Meters")
        print("\n")

    def getSpeed(self):
        return self.__speed
    
    def getHeight(self):
        return self.__height
