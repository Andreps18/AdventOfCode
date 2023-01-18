import numpy as np

assignments = []

with open("day4.input", "r") as file:
	for line in file.readlines():
		current = line.replace("\n",'').split(',')
		assignments.append([e.split('-') for e in current])

assignments = np.array(assignments, dtype=int)

#checks if range a is inside range b, both are lists
def is_in(a, b):
	if (a[0]>=b[0]) and (a[1]<=b[1]):
		return True
	return False

#checks if a overlaps b on the left side, like a=[2,5] and b=[4,7]
def left_overlap(a, b):
	if (a[1]>=b[0]):
		return True
	return False
	
#checks if a overlaps b on the right side, like a=[2,5] and b=[0,3]
def right_overlap(a, b):
	if (a[0]<=b[1]):
		return True
	return False
	
count = 0
for assign in assignments:
	if is_in(assign[0], assign[1]) or is_in(assign[1], assign[0]):
		count+=1
	elif left_overlap(assign[0], assign[1]):
		count +=1
	# elif left_overlap(assign[1], assign[0]):
	# 	count +=1
	elif right_overlap(assign[0], assign[1]):
		count +=1
	# elif right_overlap(assign[1], assign[0]):
	# 	count +=1

print(count)