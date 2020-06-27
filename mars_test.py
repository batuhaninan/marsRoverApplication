from Plateau import Plateau
from Rover import Rover
import unittest

class MarsRoverTest(unittest.TestCase):

    def test_inst_1(self):
        plateau = Plateau(size=(5,5), test=True, printStage=False)
        rover = Rover(plateau=plateau, position=(2,3))

        insts, ans = "LMLMLMLMM", (2,3)
        y, x = rover.instructions(insts)

        self.assertEqual((y,x), ans)


    def test_inst_2(self):
        plateau = Plateau(size=(5,5), test=True, printStage=False)
        rover = Rover(plateau=plateau, direction="e", position=(3,3))
        
        insts, ans = "MMRMMRMRRM", (5,5)

        y, x = rover.instructions(insts)

        self.assertEqual((y,x), ans)
    
if __name__ == "__main__":
    unittest.main()
