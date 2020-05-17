from Plato import Plato

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    HEADER = '\033[95m'
    WARNING = '\033[93m'


class MarsRoverTest:
        
    def __init__(self, size=(5,5), position=(2,3), direction="n", center=False, printStage=False, deleteOnInstruction=True, test=True):
        self.mars_rover = Plato(size=size, position=position, direction=direction, center=center, printStage=printStage, deleteOnInstruction=deleteOnInstruction, test=test)
        print()
    
    # Run Single Test
    def test(self, inst, ans):
        
        y, x = self.mars_rover.instructions(inst)
                
        results = {
            inst : (y,x ) == ans
        }

        self.printResults(results)

    
    # Run Multiple Tests
    def tests(self, insts, ans):
        if len(insts) != len(ans):
            return None
        
        results = {}

        for i, inst in enumerate(insts):

            y, x = self.mars_rover.instructions(inst)

            if (y, x) == ans[i]:
                results[inst] = True
            else:
                results[inst] = False

        self.printResults(results)

    # Print results
    def printResults(self, results):
        
        for k, v in results.items():
            if v:
                print(Colors.HEADER + f"Instruction(s) {Colors.WARNING + k + Colors.HEADER} Result => " + Colors.ENDC + Colors.OKGREEN + str(v) +  u' \u2713' + Colors.ENDC)

            if not v:
                print(Colors.HEADER + f"Instruction(s) {Colors.WARNING + k + Colors.HEADER} Result => " + Colors.ENDC + Colors.FAIL + str(v) + " x" + Colors.ENDC)
            print()


def runFirstCase():
    testMarsRover = MarsRoverTest(size=(5,5), position=(2,3))
    
    testMarsRover.test("LMLMLMLMM", (1,3))


def runSecondCase():
    testMarsRover = MarsRoverTest(size=(5,5), position=(3,3))

    testMarsRover.test("MMRMMRMRRM", (1,5))



if __name__ == "__main__":
    runFirstCase()
    runSecondCase()
    