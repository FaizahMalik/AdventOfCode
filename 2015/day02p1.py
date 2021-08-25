def calc_wrapping(dimensions):
    dimensions_list = dimensions.splitlines()
    total_area = 0
    for items in dimensions_list:
        split_items = items.split("x")
        i = [int(item) for item in split_items]
        area_list = [i[0] * i[1], i[1] * i[2], i[2] * i[0]]
        surface_area = sum([i * 2 for i in area_list])
        slack_area = min(area_list)
        total_area += slack_area + surface_area
    return total_area


# print(calc_wrapping("2x3x4\n1x2x3"))

f = open('inputs/day02input.txt', 'r')
print(calc_wrapping(f.read()))
