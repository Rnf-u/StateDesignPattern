import unittest
from Light import *
from State import *


class TestBuilder(unittest.TestCase):
    def test_if_state_is_change_on(self):

        # ARRANGE
        expectedState = OnTrafficState()

        # ACT
        tl = Light()
        tl.state.doAction()
        lighton = tl.Light(OnTrafficState)

        # ASSERT
        self.assertEqual(lighton.onState, expectedState)

    def test_if_state_is_off(self):

        # ARRANGE
        expectedState = OffTrafficState()

        # ACT
        tl = Light()
        tl.state.doAction()
        lightoff = tl.Light(OffTrafficState)

        # ASSERT
        self.assertEqual(lightoff.offState, expectedState)


if __name__ == '__main__':
    unittest.main()
