def floor_finder(santapath):
    santapathList = list(santapath)
    current_floor = 0
    for i, c in enumerate(santapathList):
        if c == "(":
            current_floor += 1
        elif c == ")":
            current_floor -= 1
            if current_floor == -1:
                return i+1
        else:
            return "floor is never reached"

f = open("inputs/day01input.txt", "r")
print(floor_finder(f.read()))

