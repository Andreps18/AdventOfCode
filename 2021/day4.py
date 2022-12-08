import numpy as np
import time
numbers = []
boards = []
# Part1
# for num in numbers:
#     for index in range(boards.shape[0]):
#         boards[index] = np.where(boards[index]==num, -1, boards[index])

#         if checkBingo(boards[index]):
#             # print("yay", boards[index])
#             sum = 0
#             for row in boards[index]:
#                 for element in row:
#                     if element != -1:
#                         sum += element
            
#             print(f"score is {sum*num}")
#             exit()

class bingo():
    def __init__(self, board: np.array) -> None:
        self.board = board
        self.won = False

    def tagNumber(self, num):
        self.board = np.where(self.board==num, -1, self.board)
    
    def computeScore(self, num):
        sum = 0
        for row in self.board:
            for element in row:
                if element != -1:
                    sum += element
        
        return sum*num

    def checkBingo(self):
        for index, row in enumerate(self.board):
            # print(f"checking row {index}, {row}")
            if np.all(row==row[0]) == True:
                if row[0] == -1:
                    self.won = True
                    return True
        
        for index, col in enumerate(self.board.T):
            if np.all(col==col[0]) == True:
                if col[0] == -1:
                    self.won = True
                    return True
        
        return False

with open("day4.input", "r") as file:
    numbers = file.readline().split(",")
    
    #load the boards (5 by 5 grid)
    currentboard = []
    counter = 0
    for line in file.readlines():
        if line!="\n":
            counter+=1
            currentboard.append(line.split())
            if counter==5:
                counter = 0
                boards.append( bingo( np.array(currentboard, dtype=int) ) )
                currentboard=[]
    
    numbers = np.array(numbers, dtype=int)

lastScore = 0
for num in numbers:
    for index, board in enumerate(boards):
        boards[index].tagNumber(num)
        
        if boards[index].won == False:
            if boards[index].checkBingo():  
                print(f"board {index} won when {num} was drawn")          
                lastScore = boards[index].computeScore(num)

print(lastScore)