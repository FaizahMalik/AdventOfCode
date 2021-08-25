import math

def calc_ribbon(dimensions):
    dimensions_list = dimensions.splitlines()
    total_ribbon = 0
    for items in dimensions_list:
        split_items = items.split("x")
        i = [int(item) for item in split_items]
        min_perimeter = min([i[0] * 2 + i[1] * 2, i[1] * 2 + i[2] * 2, i[2] * 2 + i[0] * 2])
        slack = math.prod(i)
        total_ribbon += min_perimeter + slack
    return total_ribbon

f = open('inputs/day02input.txt', 'r')
print(calc_ribbon(f.read()))

