import numpy as np
import time

from numpy import linalg

numbers = []
with open("day5.input", "r") as file:
    for line in file.readlines():
        # a = 
        # b = [ element.split(",") for element in a]
        numbers.append([ element.split(",") for element in line.strip().split(" -> ") ])

numbers = np.array(numbers, dtype=int)

def findMax(numbers, axis):
    max_x = 0
    if axis == "x":
        for line in numbers:
            for coord in line:
                max_x = max(coord[0], max_x)
    elif axis == "y":
        for line in numbers:
            for coord in line:
                max_x = max(coord[1], max_x)
    return max_x

class diagIDXs():
    def __init__(self, start, end) -> None:
        if(start[0]>end[0]):
            self.x_op = np.subtract
        else:
            self.x_op = np.add

        if(start[1]>end[1]):
            self.y_op = np.subtract
        else:
            self.y_op = np.add

        self.x = start[0]
        self.y = start[1]

        self.x_end = end[0]
        self.y_end = end[1]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        x = self.x
        y = self.y
        
        self.x = self.x_op(self.x, 1)
        self.y = self.y_op(self.y, 1)

        if x == self.x_op(self.x_end, 1) and y == self.y_op(self.y_end, 1):
            raise StopIteration

        return [x,y]


def isLine(coords):
    if coords[0][0] == coords[1][0]: #pontos teem a mesma coordenada y
        return "y"
    
    if coords[0][1] == coords[1][1]: #pontos teem a mesma coordenada x
        return "x"
    
    if abs(coords[0][0] - coords[1][0]) == abs(coords[0][1] - coords[1][1]): #pontos alinhados diagonalmente
        return "d"
    return False

def getLine(coords):
    if isLine(coords) == "x":
        if coords[0][0] > coords[1][0]:
            iterations = range(coords[1][0], coords[0][0]+1)
        else:
            iterations = range(coords[0][0], coords[1][0]+1)

        linePoints = [ [i, coords[0][1]] for i in iterations ]
        return linePoints
    
    elif isLine(coords) == "y":
        if coords[0][1] > coords[1,1]:
            iterations = range(coords[1][1], coords[0][1]+1)
        else:
            iterations = range(coords[0][1], coords[1][1]+1)

        linePoints = [ [coords[0][0], i] for i in iterations ]
        return linePoints
    
    elif isLine(coords) == "d":
        iterations = diagIDXs(coords[0], coords[1])
        linePoints = list(iterations)
        return linePoints
    
    return None


board = np.zeros((findMax(numbers, "x")+1, findMax(numbers, "y")+1))

for coords in numbers:
    linePoints = getLine(coords)
    if linePoints != None:
        #mark this points in board
        for point in linePoints:
            board[point[0]][point[1]] +=1

# print(board)

#count how many elements are greater than 1
count = 0
for element in board.flatten():
    if element > 1:
        count+=1

print(count)