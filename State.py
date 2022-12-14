from Light import *
from time import sleep


class ITrafficState:
    def doAction(self):
        pass

    def toggleState():
        pass


class OnTrafficState(ITrafficState):
    # ARRANGE
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            #this executes when there is no instance yet, so it creates a new instance
            cls.instance = super(OnTrafficState, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.states = {"STOP": 10, "GO": 20, "SLOW DOWN": 5}

    # ACT
    def timer(self):
        for x, y in self.states.items():
            print("------", x, "-------")
            for i in range(y, 0, -1):
                print("%d..." % i)
                sleep(1)

    def doAction(self):
        print("TRAFFIC LIGHT ON!")

    def toggleState(self, light):
        print("SWITCHING OFF...")
        light.state = light.offState


class OffTrafficState(ITrafficState):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            #this executes when there is no instance yet, so it creates a new instance
            cls.instance = super(OffTrafficState, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.states = ["ON"]

    # ASSERT
    def doAction(self):
        print("TRAFFIC LIGHT OFF!")

    def toggleState(self, light):
        print("SWITCHING ON...")
        light.state = light.onState
