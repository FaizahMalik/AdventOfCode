f = open("inputs/day01input.txt")

caloriesList = f.read().split('\n\n')

caloriesList = list(map(lambda dailyCalories: list(map(int, dailyCalories.split('\n'))), caloriesList))

print(caloriesList)
dailyCalories = []
for i in caloriesList:
    dailyCalories.append(sum(i))

# method 1
top3 = 0
for i in range(3):  # range is stupid and does not start from 0
    top3 += max(dailyCalories)
    dailyCalories.remove(max(dailyCalories))
print(top3)

# method 2
dailyCalories.sort()
print(sum(dailyCalories[-3:]))
