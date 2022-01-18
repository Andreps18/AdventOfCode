import numpy as np

with open("day7.input", "r") as file:
    positions = [int(num) for num in file.readline().strip().split(",")]

positions = np.array(positions, dtype=int)

# print(np.median(positions))
# print(f"Gives total of {np.sum(abs(positions - np.median(positions)))} fuel")


#parte2 faz sentido ser a media??
#floor ou ceil?
destination = np.floor(np.mean(positions))
print(f"goes to {destination}")

#find the distance of the points to the destination
# print(positions)
distances = abs(positions - destination)
# print(distances)
fuel = 0
for i in range(int(max(distances))):
    non_zero_dists = np.count_nonzero(distances)
    fuel += (i+1)*non_zero_dists
    
    distances = np.where(distances!=0, distances-1, 0)

print(f"part2 Gives total of {fuel} fuel")
