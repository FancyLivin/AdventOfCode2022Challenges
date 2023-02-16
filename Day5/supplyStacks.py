##### PART 1 #####
def stackSortOne():
    file = open("supplyStacks.txt", "r")
    
    tempString = file.readline()
    totalStacks = len(tempString)//4
    nestedStack = [[]*totalStacks for iterator in range(totalStacks)]

    file.close()

    file = open("supplyStacks.txt", "r")

    for x in file:
        if x[:5] == 'move ':
            # Command to grab from text file to move objects to new stack
            command = x[5:]
            # Splits the command into its 3 separate values
            totalMoves = int(command.partition('from')[0])
            startStack = int(command.partition('to')[0].partition('from')[2]) - 1
            destStack = int(command.partition('to')[2]) - 1
            
            # Logic for stack movement
            for iterator in range(totalMoves):
                if len(nestedStack[startStack]) != 0:
                    val = nestedStack[startStack].pop(0)
                    nestedStack[destStack].insert(0, val)
            
        elif len(x) > 1:
            # When reading each stack's number
            if x[1] == '1':
                None
            # Storing values in appropriate stacks
            else:
                currentStack = 0
                # 1, 5, 9 store values (every 4 stores value)
                for count, char in enumerate(x):
                    if count % 4 == 1:
                        if char == ' ':
                            None
                        else:
                            nestedStack[currentStack].append(char)
                        currentStack += 1

                None
    
    stackOutput = ''
    for x in range(len(nestedStack)):
        if len(nestedStack[x]) != 0:
            stackOutput += nestedStack[x][0]
    return stackOutput

    # return nestedStack

##### PART 2 #####
def stackSortTwo():
    file = open("supplyStacks.txt", "r")
    
    tempString = file.readline()
    totalStacks = len(tempString)//4
    nestedStack = [[]*totalStacks for iterator in range(totalStacks)]

    file.close()

    file = open("supplyStacks.txt", "r")

    for x in file:
        if x[:5] == 'move ':
            # Command to grab from text file to move objects to new stack
            command = x[5:]
            # Splits the command into its 3 separate values
            totalMoves = int(command.partition('from')[0])
            startStack = int(command.partition('to')[0].partition('from')[2]) - 1
            destStack = int(command.partition('to')[2]) - 1

            # Logic for stack movement
            for iterator in range(totalMoves):
                if len(nestedStack[startStack]) != 0 :
                    val = nestedStack[startStack].pop(totalMoves - iterator - 1)
                    nestedStack[destStack].insert(0, val)
            
        elif len(x) > 1:
            # When reading each stack's number
            if x[1] == '1':
                None
            # Storing values in appropriate stacks
            else:
                currentStack = 0
                # 1, 5, 9 store values (every 4 stores value)
                for count, char in enumerate(x):
                    if count % 4 == 1:
                        if char == ' ':
                            None
                        else:
                            nestedStack[currentStack].append(char)
                        currentStack += 1

                None
    
    stackOutput = ''
    for x in range(len(nestedStack)):
        if len(nestedStack[x]) != 0:
            stackOutput += nestedStack[x][0]
    return stackOutput

    # return nestedStack

##### PART 1/2 OUTPUT #####
print("Part one answer: " + stackSortOne())
print("Part two answer: " + stackSortTwo())