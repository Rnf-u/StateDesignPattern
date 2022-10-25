from Light import *

def toggleTrafficLight(light):
    light.toggleState()
    light.state.doAction()

light = Light()
light.state.doAction()

choice = int(input("Do you want to turn on the traffic light? (1=YES, 0=NO): "))

if choice == 1:
    toggleTrafficLight(light)
    light.state.timer()
    toggleTrafficLight(light)
else:
    print("CURRENT STATE: ")
    light.state.doAction()