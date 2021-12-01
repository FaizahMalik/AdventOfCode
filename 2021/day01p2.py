
f = open("inputs/day01input.txt", "r")

class Submarine:
    def __init__(self, rawDepths):
            self.rawDepths = rawDepths
            self.listOfDepths = list(map(int, self.rawDepths.split("\n")))
            self.processedDepths = self.listOfDepths

    def increasingDepths(self):
        increasingAmount = 0
        for i, v in enumerate(self.processedDepths):
            if i > 0 and v > self.processedDepths[i-1]:
                increasingAmount += 1
        return increasingAmount


    def slidingWindow(self):
        self.processedDepths = []
        for i, v in enumerate(self.listOfDepths):
            sumOf3 = sum(self.listOfDepths[i: i+3])
            self.processedDepths.append(sumOf3)


sub01 = Submarine(f.read())

sub01.slidingWindow()
print(sub01.increasingDepths())


# f.seek(0)
# filedata = f.read()
# data = list(map(int, filedata.split("\n")))
# prevDepth = data.pop()
# results = 1
#
# for i in range(len(data)-2):
#     depth = data[i] + data[i+1] + data[i+2]
#     if depth > prevDepth:
#         results+=1
#
#     prevDepth = depth
#
# print(results)