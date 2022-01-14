f = open("inputs/day02input.txt", "r")

class Navigation:
    def __init__(self, directions):
        self.directions = directions
        self.listOfDirections = self.directions.split("\n")
        self.horizontalPosition = 0
        self.depth = 0


    def calculatePosition(self):
        for i in self.listOfDirections:
            magnitude = int(''.join(filter(str.isdigit, f'{i}')))
            if 'forward' in i:
                self.horizontalPosition += magnitude
            elif 'down' in i:
                self.depth += magnitude
            elif 'up' in i:
                self.depth -= magnitude
            else:
                return False and 'unrecognised direction'
        return True

    def getPosition(self):
        return self.horizontalPosition, self.depth

    def multiplyPosition(self):
        return self.horizontalPosition * self.depth


t01 = Navigation(f.read())
print(t01.calculatePosition())
print(t01.getPosition())
print(t01.multiplyPosition())