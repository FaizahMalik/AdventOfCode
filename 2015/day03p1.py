f = open("inputs/day03input.txt", "r")

class presentguy:
    def __init__(self, directions):
        self.directions = directions
        self.locationsList = [(0, 0)]  # (x, y). +> +^

    
    def locations(self):
        for i, v in enumerate(self.directions):
            if v == ">":
                temp = [(self.locationsList[i][0] + 1), (self.locationsList[i][1])]
            elif v == "<":
                temp = [(self.locationsList[i][0] - 1), (self.locationsList[i][1])]
            elif v == "^":
                temp = [(self.locationsList[i][0]), (self.locationsList[i][1] + 1 if v == "v" else - 1)]
            elif v == "v":
                temp = [(self.locationsList[i][0]), (self.locationsList[i][1] - 1)]

            self.locationsList.append(tuple(temp))
        return self.locationsList
    
    
    def newHouses(self):
        newLocations = set(self.locationsList)
        return len(newLocations)


huh = presentguy(f.read())

huh.locations()
print(huh.newHouses())

