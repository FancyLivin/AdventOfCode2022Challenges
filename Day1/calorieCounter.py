##### PART 1 #####
def maxCaloriesOne():
    file = open("calories.txt", "r")

    maxCal = 0
    currentElfCal = 0

    for x in file:
        if x != "\n":
            currentElfCal += int(x)
        else:
            if maxCal < currentElfCal:
                maxCal = currentElfCal
            currentElfCal = 0
    return maxCal

##### PART 2 #####
def maxCaloriesTwo():
    file = open("calories.txt", "r")

    maxCal1 = 0
    maxCal2 = 0
    maxCal3 = 0
    currentElfCal = 0

    for x in file:
        if x != "\n":
            currentElfCal += int(x)
        else:
            if maxCal1 < currentElfCal:
                maxCal3 = maxCal2
                maxCal2 = maxCal1
                maxCal1 = currentElfCal
            elif maxCal2 < currentElfCal:
                maxCal3 = maxCal2
                maxCal2 = currentElfCal
            elif maxCal3 < currentElfCal:
                maxCal3 = currentElfCal
            currentElfCal = 0

    return maxCal1 + maxCal2 + maxCal3


print(maxCaloriesOne())
print(maxCaloriesTwo())