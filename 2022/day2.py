import numpy as np

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

SCORES= {
	ROCK: 1,
	PAPER: 2,
	SCISSORS: 3
}

moves = []

with open("day2.input", "r") as file:
	for line in file.readlines():
		moves.append( line.replace('\n','').split(' '))

score = 0

for play in moves:
	if play[1] == 'X': #lose
		score += 0
		if play[0] == ROCK:
			score += SCORES[SCISSORS]
		elif play[0] == SCISSORS:
			score += SCORES[PAPER]
		elif play[0] == PAPER:
			score += SCORES[ROCK]
	elif play[1] == 'Y': #draw
		score += 3
		#play the same
		score += SCORES[play[0]] 
	elif play[1] == "Z": #win
		score += 6
		if play[0] == ROCK:
			score += SCORES[PAPER]
		elif play[0] == SCISSORS:
			score += SCORES[ROCK]
		elif play[0] == PAPER:
			score += SCORES[SCISSORS]

print(score)


# def evaluate(player, opponent):
# 	#draw
# 	if player == opponent:
# 		return 3
	
# 	if player == ROCK:
# 		if opponent == SCISSORS:
# 			return 6
# 		else:
# 			return 0
		
# 	if player == SCISSORS:
# 		if opponent == PAPER:
# 			return 6
# 		else:
# 			return 0
		
# 	if player == PAPER:
# 		if opponent == ROCK: 
# 			return 6
# 		else:
# 			return 0