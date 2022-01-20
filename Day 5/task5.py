import numpy as np

class inputValue:
    x1 = 0,
    y1 = 0,
    x2 = 0,
    y2 = 0

class board:
    ventTrackingBoard = []
    def __init__(self, boardWidth, boardLength):
        tempBoard = []
        for row in range(0, (boardLength+1)):
            tempLine = [0] * (boardWidth+1)
            tempBoard.append(tempLine)
        self.ventTrackingBoard= np.array(tempBoard)

def cleanInputs(rawInput):
    cleanedInputs = []
    for line in rawInput:
        temp = line.replace(" ", "")
        temp = line.replace("\n", "")
        temp = temp.split("->")

        newInputValue = inputValue()

        newInputValue.x1 = int(temp[0].split(",")[0])
        newInputValue.y1 = int(temp[0].split(",")[1])
        newInputValue.x2 = int(temp[1].split(",")[0])
        newInputValue.y2 = int(temp[1].split(",")[1])
        # print(newInputValue.x1, " ", newInputValue.y1, " ",newInputValue.x2, " ",newInputValue.y2)

        cleanedInputs.append(newInputValue)
    return cleanedInputs

def findBoardEdges(cleanedInputs):
    maxX = 0
    maxY = 0
    for input in cleanedInputs:
        if input.x1 > maxX:
            maxX = input.x1
        if input.x2 > maxX:
            maxX = input.x2
        if input.y1 > maxY:
            maxY = input.y1
        if input.y2 > maxY:
            maxY = input.y2
    return maxX, maxY

def countDangerousAreas(board, threshold):
    dangerousAreas = 0
    for row in board:
        for cell in row:
            if cell >= threshold:
                dangerousAreas += 1
    return dangerousAreas

def manageVerticalAndHorizontalLines(cleanedInputs, ventTracker):
    for input in cleanedInputs:
        if(input.x1 == input.x2 or input.y1 == input.y2):
            if(input.x1 < input.x2):
                for i in range(input.x1, input.x2+1):
                    ventTracker.ventTrackingBoard[i, input.y1] += 1
            elif((input.x1 > input.x2)):
                for i in range(input.x2, input.x1+1):
                    ventTracker.ventTrackingBoard[i, input.y1] += 1

            elif(input.y1 < input.y2):
                for i in range(input.y1, input.y2+1):
                    ventTracker.ventTrackingBoard[input.x1, i] += 1
            else:
                for i in range(input.y2, input.y1+1):
                    ventTracker.ventTrackingBoard[input.x1, i] += 1
    return ventTracker

def manageDiagonalLines(cleanedInputs, ventTracker):
    for input in cleanedInputs:
        if(input.x1 != input.x2 and input.y1 != input.y2):
            if(input.x1 < input.x2):
                if(input.y1 < input.y2):
                    print(range(0, (input.x2-input.x1)+1))
                    for i in range(0, (input.x2-input.x1)+1):
                        ventTracker.ventTrackingBoard[input.x1+i, input.y1+i] += 1
                else:
                    print(range(0, (input.x2-input.x1)+1))
                    for i in range(0, (input.x2-input.x1)+1):
                        ventTracker.ventTrackingBoard[input.x1+i, input.y1-i] += 1
            else:
                if(input.y1 < input.y2):
                    print(range(0, (input.x1-input.x2)+1))
                    for i in range(0, (input.x1-input.x2)+1):
                        ventTracker.ventTrackingBoard[input.x1-i, input.y1+i] += 1
                else:
                    print(range(0, (input.x1-input.x2)+1))
                    for i in range(0, (input.x1-input.x2)+1):
                        ventTracker.ventTrackingBoard[input.x1-i, input.y1-i] += 1
    return ventTracker


f = open('inputData.txt','r')
# f = open('testFile.txt','r')

#clean inputs
rawInput = f.readlines()

cleanedInputs = cleanInputs(rawInput)
maxX, maxY = findBoardEdges(cleanedInputs)
ventTracker = board(maxX, maxY)

ventTracker = manageVerticalAndHorizontalLines(cleanedInputs, ventTracker)
ventTracker = manageDiagonalLines(cleanedInputs, ventTracker)

#printing values
print("\n\npre transpose: \n", ventTracker.ventTrackingBoard)

alignedVentTracker = np.transpose(ventTracker.ventTrackingBoard)
print("\n\n post transpose: \n", alignedVentTracker)

dangerousAreas = countDangerousAreas(ventTracker.ventTrackingBoard, 2)
print("number of dangerous areas: ", dangerousAreas)