import numpy as np
import pandas as pd
import csv


#part 1
df = pd.read_csv("inputData.csv" , comment='#', na_values='-', header=None)

inputs = df.iloc[:,0]

#test inputs
# inputs = [10, 11, 12, 9, 15, 13, 16, 19, 25]
# inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

larger = 0 

for i in range(1, len(inputs)):
    if (inputs[i-1] < inputs[i]):
        larger += 1

print("single larger numbers: ", larger)


#part 2 
larger = 0
for i in range(1, len(inputs) - 2):
    a = inputs[i-1] + inputs[i] + inputs[i+1]
    b = inputs[i] + inputs[i+1] + inputs[i+2]
    if (a < b):
        larger += 1


print("triple larger numbers: ", larger)


#complete