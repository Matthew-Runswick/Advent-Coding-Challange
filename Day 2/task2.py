import numpy as np
import pandas as pd
import csv


df = pd.read_csv("inputData.csv" , comment='#', na_values='-', header=None)

inputs = df.iloc[:,0]

# inputs = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

#part 1
depth = 0
horizontalPosition = 0

for i in inputs:
    splitData = i.split()
    if (splitData[0] == "forward"):
        horizontalPosition += int(splitData[1])
    elif (splitData[0] == "down"):
        depth += int(splitData[1])
    elif (splitData[0] == "up"):
        depth -= int(splitData[1])

print("------------------------ task 1 ---------------------------")
print("Horizontal Postion: ", horizontalPosition, "\nDepth: ", depth)
print("product: ", horizontalPosition * depth)

#part 2
aim = 0
depth = 0
horizontalPosition = 0

for i in inputs:
    splitData = i.split()
    if (splitData[0] == "forward"):
        horizontalPosition += int(splitData[1])
        depth += (aim * int(splitData[1]))
    elif (splitData[0] == "down"):
        aim += int(splitData[1])
    elif (splitData[0] == "up"):
        aim -= int(splitData[1])

print("\n\n------------------------ task 2 ---------------------------")
print("Horizontal Postion: ", horizontalPosition, "\nDepth: ", depth)
print("product: ", horizontalPosition * depth)

#complete 