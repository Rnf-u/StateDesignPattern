from Light import *

class ITrafficState:
    def doAction(self):
        pass

class OnTrafficState(ITrafficState):
    def __init__(self):
        self.states = ["STOP", "GO", "SLOW DOWN"]

    def doAction(self):
        print("TRAFFIC LIGHT ON!")

    def toggleState(self, light):
        print("SWITCHING OFF...")
        light.state = light.offState

class OffTrafficState(ITrafficState):
    def __init__(self):
        self.states = ["ON"]

    def doAction(self):
        print("TRAFFIC LIGHT OFF!")

    def toggleState(self, light):
        print("SWITCHING ON...")
        light.state = light.onState


