def floor_finder(upsanddowns):
    up = upsanddowns.count("(")
    down = upsanddowns.count(")")
    floor = up - down
    return floor

f = open("inputs/day01input.txt", "r")

print(floor_finder(f.read()))



