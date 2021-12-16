"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Prove 3
"""
#Class for robot movement, fire, and displaying status
class Robot:
    #Initializer method
    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100

    #Method for movement if the amount of fuel allows
    def move(self, direction):
        if self.fuel >= 5:
            self.fuel -= 5
            if direction == "left" and self.x != 0:
                self.x -= 1
            elif direction == "right":
                self.x += 1
            elif direction == "up" and self.x != 0:
                self.y -= 1
            elif direction == "down":
                self.y += 1
        else:
            print("Insufficient fuel to perform action")

    #Method for fire if the ammount of fuel allows
    def fire(self):
        if self.fuel >= 15:
            print("Pew! Pew!")
            self.fuel -= 15
        else:
            print("Insufficient fuel to perform action")

    #Method for displaying the status: coordinates and amount of fuel
    def display_status(self):
        print(f"({self.x}, {self.y}) - Fuel: {self.fuel}")
    
#The main function in which the command will be entered and the corresponding class methods will be called
def main():
    command = ""
    robot = Robot()
    while command != "quit":
        command = input("Enter command: ")
        if command == "status":
            robot.display_status()
        elif command == "left" or command == "right" or command == "up" or command == "down":
            robot.move(command)
        elif command == "fire":
            robot.fire()
    print("Goodbye.")

#Running the main function
if __name__ == "__main__":
    main()