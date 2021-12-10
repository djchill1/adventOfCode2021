import init

data = init.read_data(True, )


def part1():
	for line in data:
		closing_braces = {')': '(', ']': '[', '}': '{', '>': '<'}
		open_braces = {'(': 0, '[': 0, '{': 0, '<': 0}
		print(line)
		for entry in line:
			print(entry)
			if entry in open_braces:
				open_braces[entry] += 1
			if entry in closing_braces:
				open_braces[closing_braces[entry]] -= 1
			print(open_braces)
	return False


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
