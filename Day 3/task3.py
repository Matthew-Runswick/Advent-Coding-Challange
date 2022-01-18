import numpy as np
import pandas as pd
import csv
from numpy.core import shape


def binaryToDecimal(n):
    return int(n,2)

def removeInvalidOxygenValues(modeValue, remainingValues, digit):
    if(len(remainingValues) == 1):
        return remainingValues
    else:
        oxygenValues = []

        for i in remainingValues:
            if(modeValue == i[digit]):
                oxygenValues.append(i)

        return np.array(oxygenValues)

def removeInvalidCO2Values(modeValue, remainingValues, digit):
    if(len(remainingValues) == 1):
        return remainingValues
    else:
        CO2Values = []

        for i in remainingValues:
            if(modeValue != i[digit]):
                CO2Values.append(i)

        return np.array(CO2Values)

def arrayOfBinaryToInt(array):
    binaryNumber = 0
    lengthOfNumber = len(array)
    for i in range(0, lengthOfNumber):
        if(array[i] == 1):
            binaryNumber = binaryNumber + 10**(lengthOfNumber-(i+1))
    return binaryNumber

#part 1
df = pd.read_csv("inputData.csv" , comment='#', dtype=object, header=None)

inputs = df.iloc[:,0]
# inputs = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
# print(inputs[0])
# print(type(inputs[0]))

allDigits = []
lengthOfNumber = len(inputs[0])
# print(lengthOfNumber)

for i in inputs:
    inputDigits = []
    for digit in range(0, lengthOfNumber):
        currentDigit = i[digit:digit+1]
        inputDigits.append(int(currentDigit))

    allDigits.append(inputDigits)
    # print("Input Digits: ", inputDigits)

allDigits = np.array(allDigits)

# print("All Digits: ", allDigits)
# print("All Digits: ", allDigits[:,0])

numberOfRecords = shape(allDigits)[0]

gamma = 0
epsilon = 0
for i in range(0, lengthOfNumber):
    numberOfOnes = sum(allDigits[:,i])
    # print("number of ones: ", numberOfOnes)
    if(numberOfOnes>numberOfRecords/2):
        gamma = gamma + 10**(lengthOfNumber-(i+1))
    else:
        epsilon = epsilon + 10**(lengthOfNumber-(i+1))

print("gamma: ", gamma, "\nepsilon: ", epsilon)

print(binaryToDecimal(str(gamma)), binaryToDecimal(str(epsilon)))

print("Product of gamma and epislon: ", binaryToDecimal(str(gamma)) * binaryToDecimal(str(epsilon)), "\n\n")

#part 2
remainingOxygenValues = allDigits
remainingCO2Values = allDigits

for i in range(0, lengthOfNumber):
    numberOfRecords = len(remainingOxygenValues)
    numberOfOnesOxygen = sum(remainingOxygenValues[:,i])
    # print("remaining oxygen: ", remainingOxygenValues," - ", i)
    if(numberOfOnesOxygen>=numberOfRecords/2):
        modeValue = 1
    else:
        modeValue = 0
    # print("mode value: ", modeValue, "at i: ", i)
    remainingOxygenValues = removeInvalidOxygenValues(modeValue, remainingOxygenValues, i)

    numberOfRecords = len(remainingCO2Values)
    numberOfOnesCO2 = sum(remainingCO2Values[:,i])
    # print("remaining CO2: ", remainingCO2Values," - ", i)
    if(numberOfOnesCO2>=numberOfRecords/2):
        modeValue = 1
    else:
        modeValue = 0
    # print("mode value: ", modeValue, "at i: ", i)
    remainingCO2Values = removeInvalidCO2Values(modeValue, remainingCO2Values, i)

# print("remainingOxygenValues: ", remainingOxygenValues)
# print("remainingCO2Values: ", remainingCO2Values)

binaryOxygenValue = arrayOfBinaryToInt(remainingOxygenValues[0])
binaryCO2Value = arrayOfBinaryToInt(remainingCO2Values[0])

print("oxygen value: ", binaryOxygenValue, "\nCO2 value: ",binaryCO2Value)

print(binaryToDecimal(str(binaryOxygenValue)), binaryToDecimal(str(binaryCO2Value)))
print("Product of Oxygen value and CO2 value: ", binaryToDecimal(str(binaryOxygenValue)) * binaryToDecimal(str(binaryCO2Value)))