sacos = []

with open("day3.input", "r") as file:
	for line in file.readlines():
		current = line.replace("\n", '')
		sacos.append(current)
		# length = len(current)
		# sacos.append([current[:length//2], current[length//2:]])

to_score = []

for e1, e2, e3 in zip(range(0, len(sacos), 3), range(1, len(sacos), 3), range(2, len(sacos), 3)):
	for el in sacos[e1]:
		if (el in sacos[e2]) and (el in sacos[e3]):
			to_score.append(el)
			break



# for saco in sacos:
# 	for letter in saco[0]:
# 		if letter in saco[1]:
# 			to_score.append(letter)
# 			break
		
score = 0
for el in to_score:
	if el.isupper():
		score += (ord(el)-ord('A')+27)
	elif el.islower():
		score += (ord(el)-ord('a')+1)

print(score)