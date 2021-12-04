import init
import numpy as np
import re

data = init.read_data(False, )
numbers = data[0].split(',')

def part1():
	boards = list()
	for line in [list(map(int, x.split())) for x in data[1::]]:
		if len(line) == 5:
			boards[-1].extend([int(i) for i in line])
		else:
			boards.append(list())

	# print(boards)

	for drawn_number in numbers:
		drawn_number = int(drawn_number)
		print('playing number', drawn_number)
		for board in boards:
			# print(board)
			try:
				board[board.index(drawn_number)] = -1
				# print('after', board)
				for i in range(0,5):
					if sum(board[i::5]) == -5 or sum(board[i * 5:][:5]) == -5:
						print("BINGO")
						score = str(drawn_number * sum([i if i>-1 else 0 for i in board]))
						return score
			except:
				pass


def part2():
	boards = list()
	for line in [list(map(int, x.split())) for x in data[1::]]:
		if len(line) == 5:
			boards[-1].extend([int(i) for i in line])
		else:
			boards.append(list())

	# print(boards)
	numWins = 0

	for drawn_number in numbers:
		drawn_number = int(drawn_number)
		print('playing number', drawn_number)
		for board in boards:
			# print(board)
			try:
				board[board.index(drawn_number)] = -1
				# print('after', board)
				for i in range(0, 5):
					if sum(board[i::5]) == -5 or sum(board[i * 5:][:5]) == -5:
						if numWins == len(boards)-1:
							print("BINGO")
							score = str(drawn_number * sum([i if i > -1 else 0 for i in board]))
							return score
						numWins += 1
						board.clear()
			except:
				pass


print(f'Part 1: {part1()}, Part 2: {part2()}')