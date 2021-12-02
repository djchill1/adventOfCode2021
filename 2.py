import init
import re

data = init.read_data(False, )


def part1():
	depth = 0
	distance = 0
	for instruction in data:
		direction, value = re.split(' ', instruction)
		value = int(value)
		if direction == 'forward':
			distance += value
		elif direction == 'down':
			# increase depth
			depth += value
		elif direction == 'up':
			# decrease depth
			depth -= value
		# print(depth, distance)

	return depth*distance


def part2():
	depth = 0
	distance = 0
	aim = 0
	for instruction in data:
		direction, value = re.split(' ', instruction)
		value = int(value)
		if direction == 'forward':
			distance += value
			depth += aim*value
		elif direction == 'down':
			# increase depth
			aim += value
		elif direction == 'up':
			# decrease depth
			aim -= value
		print(depth, distance, aim)

	return depth * distance


print(f'Part 1: {part1()}, Part 2: {part2()}')