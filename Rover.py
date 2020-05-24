from Plateau import Plateau

class Rover:

    def __init__(self, plateau, speed=1, direction="n", position=(0,0), center=True):
        self.plateau = plateau
        self.speed = speed
        self.plateau.setInitialPosition(position, center)
        self.direction = direction
        self.plateau.setSpeed(speed)
        self.plateau.setDirection(direction)

        self.plateau.initMap()

    def instructions(self, insts):
        return self.plateau.instructions(insts)