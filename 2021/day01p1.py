

def increasingDepths(depths):
    depthsList = list(map(int, depths.split("\n")))
    increasingAmount = 0
    for i, v in enumerate(depthsList):
        if i > 0 and v > depthsList[i-1]:
            increasingAmount += 1
    return(increasingAmount)


f = open("inputs/day01input.txt", "r")

print(increasingDepths(f.read()))

