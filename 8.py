import re
from itertools import permutations

import init

data = init.read_data(False, )


def part1():
	count = 0

	# 1 - uses 2 segments
	# 4 - uses 4 segments
	# 7 - uses 3 segments
	# 8 - uses 7 segments
	lengths = [2, 3, 4, 7]

	for entry in data:
		input_values, output_values = re.split(" \| ", entry, 2)
		output_values = re.split(" ", output_values)
		# print(output_values)

		for item in output_values:
			if len(item) in lengths:
				count += 1

	return count


def part2():
	display = {'0': 'abcefg', '1': 'cf', '2': 'acdeg', '3': 'acdfg', '4': 'bcdf', '5': 'abdfg', '6': 'abdefg',
			   '7': 'acf', '8': 'abcdefg', '9': 'abcdfg'}
	display_r = {v: k for k, v in display.items()}
	summa = 0
	# print(display_r)

	for entry in data:
		input_values, output_values = re.split(" \| ", entry, 2)
		input_values = re.split(" ", input_values)
		output_values = re.split(" ", output_values)

		for p in permutations('abcdefg'):
			mapping = dict(zip(p, list('abcdefg')))
			for value in input_values:
				check = ''.join(sorted(mapping[c] for c in value))
				if not check in display.values():
					break
			else:
				break

		summa += int(''.join(display_r[''.join(sorted(mapping[c] for c in o))] for o in output_values))

	return summa


print(f'Part 1: {part1()}, Part 2: {part2()}')
