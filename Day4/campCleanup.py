##### PART 1 #####
def cleanupOne():
    file = open("campCleanup.txt", "r")

    fullyContained = 0

    for x in file:
        sections = x.split(",")
        elfOne = sections[0].split("-")
        elfTwo = sections[1].split("-")
        
        if int(elfOne[0]) >= int(elfTwo[0]) and int(elfOne[1]) <= int(elfTwo[1]):
            fullyContained += 1
        elif int(elfTwo[0]) >= int(elfOne[0]) and int(elfTwo[1]) <= int(elfOne[1]):
            fullyContained += 1

    return fullyContained

##### PART 2 #####
def cleanupTwo():
    file = open("campCleanup.txt", "r")

    partiallyContained = 0

    for x in file:
        sections = x.split(",")
        elfOne = sections[0].split("-")
        elfTwo = sections[1].split("-")

        if int(elfTwo[0]) <= int(elfOne[0]) <= int(elfTwo[1]):
            partiallyContained += 1
        elif int(elfTwo[0]) <= int(elfOne[1]) <= int(elfTwo[1]):
            partiallyContained += 1
        elif int(elfOne[0]) <= int(elfTwo[0]) <= int(elfOne[1]):
            partiallyContained += 1
        elif int(elfOne[0]) <= int(elfTwo[1]) <= int(elfOne[1]):
            partiallyContained += 1

    return partiallyContained

##### PART 1/2 OUTPUT #####
print(cleanupOne())
print(cleanupTwo())