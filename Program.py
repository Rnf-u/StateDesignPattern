from Light import *

light = Light()
light.state.doAction()

# ASSERT
choice = int(input("Do you want to turn on the traffic light? (1=YES, 0=NO): "))

if choice == 1:
    light.toggleState()

    while (choice != 0):
        light.state.timer()
        choice = int(input("Do you want to continue? (1=YES, 0=NO): "))

        if (choice == 0):
            light.toggleState()
            break

light.state.doAction()
print("Program terminated.")
