import numpy as np
from numpy.core.numeric import ones
data = []
with open("day8.easy.input", "r") as file:
    for line in file.readlines():
        current = line.strip().split(" | ")
        data.append(current)

data = np.array(data)

for element in data:
    #map the signals and wires

    #find the output

# ones = 0
# fours = 0
# sevens = 0
# eights = 0
# for element in data:
#     for word in element[1].split():
#         if len(word) == 2:
#             ones +=1
#         elif len(word) == 4:
#             fours += 1
#         elif len(word) == 3:
#             sevens += 1
#         elif len(word) == 7:
#             eights += 1
        
# print(ones+fours+sevens+eights)

