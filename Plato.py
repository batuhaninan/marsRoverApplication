class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Plato:
    moveList = ["m", "move", "i", "ileri"]
    
    directionList = ["n", "w", "s", "e"]
    directions = {"n":1, "w":2, "s":3, "e":4}
    
    rotateList = ["l", "left", "sol", "r", "right", "sağ"]
    
    leftList = ["l", "left", "sol"]
    rightList = ["r", "right", "sağ"]
    
    printList = {1:"^",2:"<",3:"_",4:">"}
    

    def __init__(self, size=(5,5), direction="n", position=(0,0), center=True, printStage=True, deleteOnInstruction=False):
        self.printStage = printStage
        self.terminate = False
        self.size = size
        self.position = position
        self.deleteOnInstruction = deleteOnInstruction

        # Eğer direction n w s e değilse sonlandır
        try:
            self.directionList.index(direction)
        except ValueError:
            print(bcolors.FAIL + "ValueError: Please enter the initial direction correctly. ( n | w | s | e )" + bcolors.ENDC)
            exit()

        self.direction = direction
        self.map = []

        column, row = self.position
        self.position = column - 1, row - 1
        
        # Eğer center ise self.position'ı center olarak ayarla
        if center:
            self.position = (self.size[0] // 2, self.size[1] // 2)
        self._init_map(self.size, self.position)
        
        # Eğer printStage ise ekranı bastır
        if printStage:
            self._print_map()


    # Rover'ın şu anki konumunu döndür
    def getPos(self):
        for column in range(len(self.map)):
            for row in range(len(self.map[column])):
                if self.map[column][row] in [1,2,3,4]:
                    return column, row
    
    def instructions(self, instructions):
        for instruction in instructions:
            
            instruction = instruction.lower()
            
            # Eğer komut ileri ise
            if instruction in self.moveList:
                self.move()
            
            # Eğer ileri adımında hata olmuşsa sonlandır
            if self.terminate:
                return

            # Eğer komut l ya da r ise
            if instruction in self.rotateList:
                self.rotate(instruction)


            # Eğer printStage ise her stage sonunda ekrana map'i bastır
            if self.printStage:
                print("  ", bcolors.WARNING + instruction + bcolors.ENDC)
                self._print_map()
        
        # Eğer printStage değil ise map'in son şeklini bastır
        if not self.printStage:
            print(" ", *instructions)
            self._print_map()
        
        # Eğer deleteOnInstruction ise map'i restart et
        if self.deleteOnInstruction:
            self._restart_map(self.size, self.position)

        

    def move(self):
        column, row = self.getPos()
        value = self.map[column][row]

        columnPrint = column + 1
        rowPrint = row + 1

        # Eğer şuan rover n'a bakıyorsa
        if value == 1:
            # İlerlemeyi dene, olmazsa hata mesajı bastır

            try:
                if column - 1 != -1:
                    self.map[column][row] = 0
                    self.map[column - 1][row] = value
                else:
                    self.terminate = True
                    print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)
            except IndexError:
                self.terminate = True
                print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)

        # Eğer şuan rover s'a bakıyorsa
        if value == 3:
            # İlerlemeyi dene, olmazsa hata mesajı bastır

            try:
                self.map[column][row] = 0
                self.map[column + 1][row] = value
            except IndexError:
                self.terminate = True
                print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)
        
        # Eğer şuan rover w'e bakıyorsa
        if value == 2:
            # İlerlemeyi dene, olmazsa hata mesajı bastır

            try:
                if row - 1 != -1:
                    self.map[column][row] = 0
                    self.map[column][row - 1] = value
                else:
                    self.terminate = True
                    print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)
            except IndexError:
                self.terminate = True
                print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)
        
        # Eğer şuan rover e'e bakıyorsa
        if value == 4:
            # İlerlemeyi dene, olmazsa hata mesajı bastır

            try:
                self.map[column][row] = 0
                self.map[column][row + 1] = value
            except IndexError:
                self.terminate = True
                print(bcolors.FAIL + f"IndexError: You have exceeded the map limit. ( Last Pos : x = {columnPrint} , y = {rowPrint} )" + bcolors.ENDC)

    def rotate(self, direction):
        
        # Eger instruction left ise
        if direction in self.leftList:
            column, row = self.getPos()

            value = self.map[column][row]
            self.map[column][row] = value % 4 + 1
            
        # Eger instruction right ise
        if direction in self.rightList:
            column, row = self.getPos()

            value = self.map[column][row] + 3
            
            if value > 4:
                value %= 4
            
            self.map[column][row] = value

    # Map'i verilen size ve position'a göre başlat
    def _init_map(self, size, position):
        for column in range(size[0]):
            current_row = []
            for row in range(size[1]):
                if column == position[0] and row == position[1]:
                    current_row.append(self.directions[self.direction])
                else:
                    current_row.append(0)
            self.map.append(current_row)

    # Map'i verilen size ve position'a göre yenile
    def _restart_map(self, size, position):
        del self.map
        self.map = []
        self._init_map(self.size, self.position)
        print(bcolors.HEADER + "Reset\n" + bcolors.ENDC)

    # Map'i ve rover'i ekrana bastır
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