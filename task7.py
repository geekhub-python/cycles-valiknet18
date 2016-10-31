n = int(input("Введите количество дней "))
sumTrain = 10
sumTrainN = 10
lastTrain = 10
trainList = [10]

for i in range(0, 9):
    currentTrain = lastTrain + (lastTrain / 100 * 10)
    if (i < 7):
        sumTrain += currentTrain
    lastTrain = currentTrain
    trainList.append(currentTrain)

lastTrain = 10
sumTrainN = 10

for i in range(1, n):
    currentTrain = lastTrain + (lastTrain / 100 * 10)
    sumTrainN += currentTrain

lastTrain = 10
sumTrain80 = 10
countDays = 1

while sumTrain80 < 80:
    sumTrain80 += lastTrain + (lastTrain / 100 * 10)
    countDays += 1

print("Пробег лыжника за каждый день тренеровок")

for i in range(0, len(trainList)):
    print("День", i + 1, " = ", trainList[i])

print("======================================")
print("Пробег лыжника за 7 дней", sumTrain)
print("======================================")
print("Пробег лыжника за ", n, " дней", sumTrainN)
print("=====================================")
print("80 км можно пройти за ", countDays, " дней")
print("=====================================")
