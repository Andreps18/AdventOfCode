elves = [0]
with open("day1.input", "r") as file:
    for line in file.readlines():
        try:
            elves[-1] += int(line)
        except:
            elves.append(0)

elves.sort(reverse=True) #Para ficar descendente

print(sum(elves[:3]))