##### PART 1 #####
def noSpaceOne():
    file = open("noSpace.txt", "r")
    skipLineOne = file.readline()
    tree = [["/"]]
    totalDirectorySize = 0
    listedFiles = {}

    for x in file:
        if x[0:5] == '$ cd ':
            if x[5:7] == '..':
                # print('go back one dir')
                currentDir -= 1
            elif x[5] == '/':
                # print('go back to root dir')
                currentDir = 0
            else:
                # print('change dir ' + x[5:-1])
                tree.append([x[5:-1]])
                currentDir += 1
        elif x[0:4] == '$ ls':
            # print(listedFiles)
            # print('display files')
            if listedFiles != {}:
                tree.insert(-1, listedFiles)
            listedFiles = {}
        elif x[0:4] == 'dir ':
            # print('nested dir' + x[3:-1])
            listedFiles[x[4:-1]] = "dir"
        else:
            fileInfo = x.split(' ', 1)
            fileSize = fileInfo[0]
            fileName = fileInfo[1][:-1]
            # print(fileName + ' has size of ' + fileSize)
            listedFiles[fileName] = fileSize
    
    tree.append(listedFiles)
    # print(listedFiles)
    print(tree)

    file.close()
    return totalDirectorySize


##### PART 2 #####
def noSpaceTwo():

    return None


##### PART 1/2 OUTPUT ######
# print(noSpaceOne())
# print(noSpaceTwo())