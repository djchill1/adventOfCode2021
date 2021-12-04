import init
import numpy as np

data = init.read_data(True, )
numbers = data[0].split(',')

def draw_number(index, boards):
	drawn_number = numbers[index]
	print('drawing number', drawn_number)
	bingo = False
	for line in boards:
		# print(line)
		for number in line:
			# print(number)
			number = str(number)
			if number == drawn_number:
				line.remove(int(number))
				# print('removed', number, line)
		if len(line) == 0:
			print('BINGO')
			bingo = True
	return boards, bingo, drawn_number

def part1():
	boards = [list(map(int, x.split())) for x in data[1::]]
	for entry in boards:
		if entry == []:
			boards.remove([])
	# print(boards)
	i = 0
	bingo = False
	while not bingo:
		boards, bingo, drawn_number = draw_number(i, boards)
		print(boards)
		i += 1

	# find winning board
	loc = boards.index([])
	print(loc)

	winning_sum = 1
	return winning_sum * drawn_number


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')