#Import random
import random

#Create the function below:
def matrixBuilder(num):
    matrix = []

    for i in range(num):
        row = []
        
        for j in range(num):
            row.append(1)

        matrix.append(row)

    return matrix


print(matrixBuilder(3))