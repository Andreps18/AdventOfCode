forward = 0
depth = 0
with open("day2.input", "r") as file:
    for line in file.readlines():
        action, size = line.split()
        if action == "forward":
            forward += int(size)
        elif action == "down":
            depth += int(size)
        elif action == "up":
            depth -= int(size)

print(f"final {forward*depth}")


forward = 0
depth = 0
aim = 0
with open("day2.input", "r") as file:
    for line in file.readlines():
        action, size = line.split()
        if action == "forward":
            depth += (int(size) * aim)
            forward += int(size)
        elif action == "down":
            aim += int(size)
        elif action == "up":
            aim -= int(size)

print(f"final p2 {forward*depth}")