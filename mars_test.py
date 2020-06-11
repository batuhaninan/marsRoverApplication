from Plateau import Plateau
from Rover import Rover

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    HEADER = '\033[95m'
    WARNING = '\033[93m'


class MarsRoverTest:

    def __init__(self, plateau, rover):
        self.plateau = plateau
        self.rover =rover
        print()

    # Run Single Test
    def test(self, inst, ans):
        print(inst, ans)
        y, x = self.rover.instructions(inst)

        result = (y,x) == ans

        if (y, x) == (None, None):
            result = False

        self.printResult((result,inst))

    # Print results
    def printResult(self, result):
        ans = result[0]
        res = result[1]

        if ans == True:
            print(Colors.HEADER + f"Instruction(s) {Colors.WARNING + res + Colors.HEADER} Result => " + Colors.ENDC + Colors.OKGREEN + str(ans) +  u' \u2713' + Colors.ENDC)

        if ans == False:
            print(Colors.HEADER + f"Instruction(s) {Colors.WARNING + res + Colors.HEADER} Result => " + Colors.ENDC + Colors.FAIL + str(ans) + " x" + Colors.ENDC)
        print()


def runFirstCase():
    plateau = Plateau(size=(5,5), test=True, printStage=True)

    rover = Rover(plateau=plateau, position=(2,3))

    testMarsRover = MarsRoverTest(plateau, rover)

    testMarsRover.test("LMLMLMLMM", (2,3))


def runSecondCase():
    plateau = Plateau(size=(5,5), test=True, printStage=False)

    rover = Rover(plateau=plateau, direction="e", position=(3,3))

    testMarsRover = MarsRoverTest(plateau, rover)

    testMarsRover.test("MMRMMRMRRM", (5,5))


if __name__ == "__main__":
    runFirstCase()
    runSecondCase()

