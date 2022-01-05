import numpy as np
import pandas as pd
import csv
from numpy.core import shape


def binaryToDecimal(n):
    return int(n,2)

#part 1
df = pd.read_csv("inputData.csv" , comment='#', dtype=object, header=None)

inputs = df.iloc[:,0]
# inputs = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
print(inputs[0])
print(type(inputs[0]))

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
    print("number of ones: ", numberOfOnes)
    if(numberOfOnes>numberOfRecords/2):
        gamma = gamma + 10**(lengthOfNumber-(i+1))
    else:
        epsilon = epsilon + 10**(lengthOfNumber-(i+1))

print("gamma: ", gamma, "\nepsilon: ", epsilon)

print(binaryToDecimal(str(gamma)), binaryToDecimal(str(epsilon)))

print("Product of gamma and epislon: ", binaryToDecimal(str(gamma)) * binaryToDecimal(str(epsilon)))

#part 2