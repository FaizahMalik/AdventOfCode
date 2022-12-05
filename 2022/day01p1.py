# i forgot how to code lol

f = open("inputs/day01input.txt", "r")

class fatElf:
    def __init__(self, caloriesList):
        self.caloriesList = caloriesList.split('\n')


    def calorieCounter(self):
        totalCalories = []
        dailyCalories = 0

        for i in self.caloriesList:
            if i == '':
                totalCalories.append(dailyCalories)
                dailyCalories = 0
            else:
                dailyCalories += int(i)
        return max(totalCalories)

    def preview(self):
        return self.caloriesList



huh = fatElf(f.read())

print(huh.calorieCounter())

