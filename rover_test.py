import unittest
from mars_rover import Rover

# list is in format initial position, current position of rover,command and expected position
inputs_and_expected = [
    [[5,5],[1,2,'N'],['LMLMLMLMM'],[1,3,'N']],
    [[5,5],[3,3,'E'],['MMRMMRMRRM'],[5,1,'E']],
    #[[5,5],[3,3,'E'],['MMRMMRMRRM'],[5,3,'E']],
]

class RoverTestCase1(unittest.TestCase):
    def test_Rover_positions(self):
        for test_inputs in inputs_and_expected:
            rover = Rover(test_inputs[0][0],test_inputs[0][1])
            rover.set_initial_position(test_inputs[1][0],test_inputs[1][1], test_inputs[1][2])
            rover.send_command(test_inputs[2][0])
            for idx,values in enumerate(rover.get_position()):
                self.assertEqual(values,test_inputs[3][idx])


if __name__ == '__main__':
    unittest.main()
