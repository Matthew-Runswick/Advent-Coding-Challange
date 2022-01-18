import numpy as np
import pandas as pd

class bingoCard:
    numbersFound = 0
    highestLine = 0
    cardValues = []

def generateGameNumbers(rawData):
    gameNumbersString = rawData[0]
    gameNumbersString = gameNumbersString.replace("\n","")
    gameNumbers = gameNumbersString.split(",")
    temp = []
    for number in gameNumbers:
        temp.append(int(number))
    gameNumbers = temp
    return gameNumbers

def generateGameNumbersAndCards(rawData):
    gameNumbers = generateGameNumbers(rawData)

    listOfBingoCards = []
    tempBingoCard = bingoCard()
    tempCardValues = []
    for line in range(2, len(rawData)):
        currentLine = rawData[line].replace("\n","")
        if(currentLine != ""):
            tempList = currentLine.split(" ")
            tempList = list(filter(None, tempList))
            boardLine = []
            for value in tempList:
                boardLine.append([int(value), False])

            tempCardValues.append(boardLine)

        if(currentLine == ""):
            tempBingoCard.cardValues = np.array(tempCardValues)
            listOfBingoCards.append(tempBingoCard)

            tempBingoCard = bingoCard()
            tempCardValues = []

    tempBingoCard.cardValues = np.array(tempCardValues)
    listOfBingoCards.append(tempBingoCard)

    return gameNumbers, listOfBingoCards

def findNewHighestLine(bingoCard, row, column):
    higestLine = bingoCard.highestLine

    checkedValuesInCurrentLine = 0
    for i in range(0, len(bingoCard.cardValues)):
        if(bingoCard.cardValues[i][column][1] == True):
            checkedValuesInCurrentLine += 1
    if(checkedValuesInCurrentLine> higestLine):
        higestLine = checkedValuesInCurrentLine

    checkedValuesInCurrentLine = 0
    for i in range(0, len(bingoCard.cardValues[0])):   
        if(bingoCard.cardValues[row][i][1] == True):
            checkedValuesInCurrentLine += 1
    if(checkedValuesInCurrentLine> higestLine):
        higestLine = checkedValuesInCurrentLine
    
    return higestLine

def checkWin(listOfBingoCards):
    for bingoCard in listOfBingoCards:
        if(bingoCard.highestLine == 5):
            return bingoCard
    return ""

def playRound(numberCalled, listOfBingoCards):
    for bingoCard in listOfBingoCards:
        for row in range(0, len(bingoCard.cardValues)):
            for column in range(0, len(bingoCard.cardValues[0])):
                if(bingoCard.cardValues[row][column][0] == numberCalled):
                    bingoCard.cardValues[row][column][1] = True
                    bingoCard.numbersFound += 1

                    bingoCard.highestLine = findNewHighestLine(bingoCard, row, column)


    return listOfBingoCards

def playGame(gameNumbers, listOfBingoCards):
    for number in gameNumbers:
        listOfBingoCards = playRound(number, listOfBingoCards)

        winningCard = checkWin(listOfBingoCards)
        if(winningCard != ""):
            return number, winningCard

def sumOfUnmarkedNumbers(winningBoard):
    sumValue = 0
    for row in winningBoard.cardValues:
        for column in row:
            if(column[1] == False):
                sumValue += column[0]

    return sumValue


f = open('inputData.txt','r')
# f = open('testFile.txt','r')

rawData = f.readlines()

gameNumbers, listOfBingoCards = generateGameNumbersAndCards(rawData)

# print(gameNumbers)
# print(len(listOfBingoCards))

lastNumberCalled, winningBoard = playGame(gameNumbers, listOfBingoCards)

print("last number called: ", lastNumberCalled)
# print("winning board: \nhighestLine", winningBoard.highestLine, "\nnumbers found", winningBoard.numbersFound, "\ncard: \n", winningBoard.cardValues)

sumOfUnmarkedNumbers = sumOfUnmarkedNumbers(winningBoard)
print("sumOfUnmarkedNumbers: ", sumOfUnmarkedNumbers)
print("final result: ", sumOfUnmarkedNumbers * lastNumberCalled)