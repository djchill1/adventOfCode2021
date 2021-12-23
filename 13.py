import init
import re
import numpy as np

data = init.read_data(False, )

folds = []
initial_positions = []
max_x, max_y = 0, 0

for line in data:
	split = re.split(' |=|,', line)
	if split[0] == 'fold':
		folds.append((split[2], int(split[3])))
	elif split[0] == '':
		pass
	else:
		x, y = int(split[0]), int(split[1])
		if x > max_x:
			max_x = x
		if y > max_y:
			max_y = y
		initial_positions.append((x, y))


# print(folds)
# print(initial_positions)
# print(max_x, max_y)


def draw_initial_image(positions, max_x, max_y):
	paper = np.zeros((max_y + 1, max_x + 1))
	for entry in positions:
		x, y = entry[0], entry[1]
		paper[y, x] = 1
	return paper


def transform_image(paper, fold_instruction, positions):
	# figure out new size array
	axis, position = fold_instruction
	size = np.shape(paper)
	# print(size)
	if axis == 'x':
		new_size = (size[0], position)
	else:
		new_size = (position, size[1])
	# print(new_size)
	new_paper = draw_initial_image(positions, new_size[1]-1, new_size[0]-1)
	# reflect array onto itself and add values

	return new_paper


def fold_positions(positions, fold_instruction):
	axis, position = fold_instruction
	new_positions = []
	for point in positions:
		if axis == 'x':
			if point[0] > position:
				new_point = (-point[0] % position, point[1])
			else:
				new_point = point
		elif axis == 'y':
			if point[1] > position:
				new_point = (point[0], -point[1] % position)
			else:
				new_point = point
		new_positions.append(new_point)
	return new_positions


def part1(iterations):
	print('initial paper:')
	paper = draw_initial_image(initial_positions, max_x, max_y)
	print(paper)
	positions = initial_positions
	print(positions)
	iter = 0
	for fold_instruction in folds:
		print('folding:', fold_instruction)
		positions = fold_positions(positions, fold_instruction)
		paper = transform_image(paper, fold_instruction, positions)
		print('result:')
		print(positions)
		print(paper)
		iter += 1
		if iter >= iterations:
			break

	return sum(sum(paper)), paper


def part2():
	_, paper = part1(9999)

	# visualise
	display = []
	for row in paper:
		line = []
		for value in row:
			if value == 1:
				line.append('#')
			else:
				line.append(' ')
		display.append(line)

	for line in display:
		print(line)
	return False


print(f'Part 1: {part1(1)[0]}, Part 2: {part2()}')
