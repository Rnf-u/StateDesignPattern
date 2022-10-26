import unittest
from Light import *
from State import *


class TestBuilder(unittest.TestCase):
    def test_if_state_is_off(self):

        # ARRANGE
        expectedState1 = OffTrafficState()

        # ACT
        actualState1 = Light()
        #by default, is OFF

        # ASSERT
        self.assertEqual(actualState1.state, expectedState1)

    def test_if_state_is_off_to_on(self):

        # ARRANGE
        expectedState2 = OnTrafficState()

        # ACT
        actualState2 = Light()
        actualState2.toggleState()

        # ASSERT
        self.assertEqual(actualState2.state, expectedState2)
        #must all be ON

    def test_if_state_is_on_to_off(self):
         # ARRANGE
        expectedState3 = OffTrafficState()

        # ACT
        actualState3 = Light()
        actualState3.toggleState()
        actualState3.toggleState()

        # ASSERT
        self.assertEqual(actualState3.state, expectedState3)
        #must all be OFF


if __name__ == '__main__':
    unittest.main()
