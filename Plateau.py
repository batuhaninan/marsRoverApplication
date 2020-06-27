class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Plateau:
    moveList = ["m", "move", "i", "ileri"]

    directionList = ["n", "w", "s", "e"]
    directions = {"n":1, "w":2, "s":3, "e":4}

    rotateList = ["l", "left", "sol", "r", "right", "sağ"]

    leftList = ["l", "left", "sol"]
    rightList = ["r", "right", "sağ"]

    printList = {1:"^",2:"<",3:"V",4:">"}


    def __init__(self, size=(5,5), printStage=False, deleteOnInstruction=True, test=False):
        self.printStage = printStage
        self.terminate = False
        self.size = size
        self.deleteOnInstruction = deleteOnInstruction
        self.test = test

        self.map = []


    def initMap(self):
        self._init_map(self.size, self.position)

        if self.printStage:
            self._print_map()

    def setInitialPosition(self, position, center):
        self.position = position
        self.center = center

        column, row = self.position
        self.position = column - 1, row - 1

        if center:
            self.position = (self.size[0] // 2, self.size[1] // 2)


    def setSpeed(self, speed):
        self.speed = speed

    def setDirection(self, direction):
        self.direction = direction

        try:
            self.directionList.index(direction)
        except ValueError:
            print(bcolors.FAIL + "ValueError: Please enter the initial direction correctly. ( n | w | s | e )" + bcolors.ENDC)
            exit()


    def getPos(self):
        for column in range(len(self.map)):
            for row in range(len(self.map[column])):
                if self.map[column][row] in [1,2,3,4]:
                    return column, row

    def instructions(self, instructions):
        for instruction in instructions:

            instruction = instruction.lower()

            if instruction in self.moveList:
                self.move()

            if self.terminate:
                return (None,None)

            if instruction in self.rotateList:
                self.rotate(instruction)


            if self.printStage:
                print("  ", bcolors.WARNING + instruction + bcolors.ENDC)
                self._print_map()

        if not self.printStage and not self.test:
            print(" ", *instructions)
            self._print_map()

        y, x = self.getPos()
        y, x = y+1, x+1


        if self.deleteOnInstruction:
            self._restart_map(self.size, self.position)

        return y, x



    def move(self):
        column, row = self.getPos()
        value = self.map[column][row]

        columnPrint = column + 1
        rowPrint = row + 1

        if value == 1:

            try:
                if column - self.speed != -1:
                    self.map[column][row] = 0
                    self.map[column - self.speed][row] = value
                else:
                    self.terminate = True
                    print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)
            except IndexError:
                self.terminate = True
                print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)

        if value == 3:

            try:
                self.map[column][row] = 0
                self.map[column + self.speed][row] = value
            except IndexError:
                self.terminate = True
                print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)

        if value == 2:

            try:
                if row - self.speed != -1:
                    self.map[column][row] = 0
                    self.map[column][row - self.speed] = value
                else:
                    self.terminate = True
                    print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)
            except IndexError:
                self.terminate = True
                print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)

        if value == 4:

            try:
                self.map[column][row] = 0
                self.map[column][row + self.speed] = value
            except IndexError:
                self.terminate = True
                print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)

    def rotate(self, direction):

        if direction in self.leftList:
            column, row = self.getPos()

            value = self.map[column][row]
            self.map[column][row] = value % 4 + 1

        if direction in self.rightList:
            column, row = self.getPos()

            value = self.map[column][row] + 3

            if value > 4:
                value %= 4

            self.map[column][row] = value

    def _init_map(self, size, position):
        for column in range(size[0]):
            current_row = []
            for row in range(size[1]):
                if column == position[0] and row == position[1]:
                    current_row.append(self.directions[self.direction])
                else:
                    current_row.append(0)
            self.map.append(current_row)

    def _restart_map(self, size, position):
        del self.map
        self.map = []
        self._init_map(self.size, self.position)

        if not self.test:
            print(bcolors.HEADER + "Reset\n" + bcolors.ENDC)

    def _print_map(self):
        print("  ", end="")
        print((bcolors.OKBLUE + "- " + bcolors.ENDC) * len(self.map))


        for column in range(len(self.map)):
            print(bcolors.OKBLUE + "|" + bcolors.ENDC, end=" ")
            for row in range(len(self.map[column])):
                value = self.map[column][row]
                if value != 0:
                    value = self.printList[value]
                    print(bcolors.WARNING + str(value) + bcolors.ENDC, end=" ")
                else:

                    print(bcolors.HEADER + str(value) + bcolors.ENDC, end=" ")
            if column + 1 != len(self.map):
                print(bcolors.OKBLUE + "|" + bcolors.ENDC, end="\n\n")
            else:
                print(bcolors.OKBLUE + "|" + bcolors.ENDC)
        print("  ", end="")
        print((bcolors.OKBLUE + "- " + bcolors.ENDC) * len(self.map))
        print("\n\n")
