from State import *


class Light:
    # ARRANGE
    def __init__(self):
        self.onState = OnTrafficState()
        self.offState = OffTrafficState()
        self.state = self.offState

    def toggleState(self):
        self.state.toggleState(self)
