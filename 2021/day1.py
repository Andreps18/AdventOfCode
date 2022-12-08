prev = 0
current = 0
increased= 0
with open("day1.input", "r") as file:
    for line in file.readlines():
        current = int(line)
        if current > prev and prev != 0:
            increased+=1
        
        prev = current

print(f"Part1 Increased: {increased}")

prev = 0
current = 0
increased= 0
with open("day1.input", "r") as file:
    lines = file.readlines()
    for index in range(len(lines)):
        try:
            current = int(lines[index]) + int(lines[index+1]) + int(lines[index+2])
        except IndexError:
            break
        
        if current > prev and prev != 0:
            increased+=1
        
        prev = current

print(f"Part2 Increased: {increased}")