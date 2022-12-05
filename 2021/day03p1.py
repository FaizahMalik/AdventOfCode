f = open("inputs/day03input.txt", "r")

class Diagnostic:
    def __init__(self, report):
        self.report = report
        self.binaryList = self.report.split("\n")
        self.gammaRateBinary = ''
        self.gammaRateDecimal = 0
        self.epsilonRateBinary = ''
        self.epsilonRateDecimal = 0
        self.numberOfItems = len(self.binaryList)
        self.count = [0] * len(self.binaryList[0])  # Number of zeros in each position

    def countZeros(self):
        for item in self.binaryList:
            for key, value in enumerate(item):
                if value == '0':
                    self.count[key] += 1

    def calculateRates(self):
        for i in self.count:
            if i > (self.numberOfItems/2):
                self.gammaRateBinary += '0'
                self.epsilonRateBinary += '1'
            else:
                self.gammaRateBinary += '1'
                self.epsilonRateBinary += '0'


    def convertRates(self):
        self.epsilonRateDecimal = int(self.epsilonRateBinary, 2)
        self.gammaRateDecimal = int(self.gammaRateBinary, 2)

    def multiplyRates(self):
        return self.epsilonRateDecimal * self.gammaRateDecimal





test01 = Diagnostic(f.read())
test01.countZeros()
test01.calculateRates()
test01.convertRates()
print(test01.multiplyRates())
