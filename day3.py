import numpy as np

data = []
with open("day3.input", "r") as file:
    for line in file.readlines():
        data.append( [char for char in line if char != "\n"] )

data = np.array( data, dtype=int )
# gama = []
# epsilon = []
# for i in range(data.shape[1]):
#     counts = np.bincount(data[:,i])
#     gama.append(np.argmax(counts))
#     epsilon.append(np.argmin(counts))
    
# gama = int("".join(str(x) for x in gama), 2)
# epsilon = int("".join(str(x) for x in epsilon), 2)

# print(gama*epsilon)

######################
def binArrayToDEC(array):
    return int("".join(str(x) for x in array), 2)

def findCommonValue(array, type="most"):
    counts = np.bincount(array)

    if type == "most":
        if np.argmax(counts) == np.argmin(counts):
            return 1
        return np.argmax(counts)
    else:
        if np.argmax(counts) == np.argmin(counts):
            return 0
        return np.argmin(counts)

oxigen = data
for i in range(12):
    mcv = findCommonValue(oxigen[:,i], "most")
    #find indexes of numbers that have mcv in index i
    idxs=[]
    for index, element in enumerate(oxigen[:,i]):
        if element== mcv:
            idxs.append(index)
    
    #remove those indexes
    oxigen = np.delete(oxigen, idxs, 0)
    if oxigen.shape[0] == 1:
        break

print(oxigen.shape)

co2 = data
for i in range(12):
    lcm = findCommonValue(co2[:,i], "least")
    #find indexes of numbers that have lcm in index i
    idxs=[]
    for index, element in enumerate(co2[:,i]):
        if element== lcm:
            idxs.append(index)
    
    #remove those indexes
    co2 = np.delete(co2, idxs, 0)
    if co2.shape[0] == 1:
        break
print(co2.shape)

prod = binArrayToDEC(co2.flatten()) * binArrayToDEC(oxigen.flatten())

print(prod)