from os import stat
import numpy as np

with open("day6.easy.input", "r") as file:
    state = [int(num) for num in file.readline().strip().split(",")]

lanternfish = [0 for _ in range(9)]

for num in state:
    lanternfish[num] += 1

print(lanternfish)
#existem lanternfish[i] peixes com idade i

days = 256
for day in range(days):
    #a cada dia faz se uma especie de shift left
    #tira-se os q teem 0 de idade e acrescenta-se esses a idade 8

    #remover o q tem 0
    removed = lanternfish.pop(0)
    
    #the zeros became 6s
    lanternfish[6] += removed

    #add #removed 8s
    lanternfish.append(removed)

print( sum(lanternfish) )

#very slow
# days = 80
# state = np.array(state)
# print(state.shape)
# for i in range(days):
#     print(f"day {i}")
#     state = state - 1
#     adds = np.count_nonzero(state==-1)
#     state = np.append(state, np.full(adds, 8))
#     # for _ in range(adds):
#     #     state = np.append(state, 8)
#     #replace the -1 with 6
#     state = np.where(state==-1, 6, state)

# print(state.shape)
