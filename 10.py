import init

data = init.read_data(False, )


def part1():
	closing_braces = {')': '(', ']': '[', '}': '{', '>': '<'}
	open_braces = {'(': 0, '[': 0, '{': 0, '<': 0}

	score = {')': 3, ']': 57, '}': 1197, '>': 25137}
	scores = []
	illegals = []

	for line in data:
		print(line)
		chunks = []
		for entry in line:
			print(entry)
			if entry in open_braces:
				chunks.append(entry)
			elif entry in closing_braces:
				# what should the most recent chunk be:
				should_be = closing_braces[entry]
				recent_is = chunks.pop(-1)
				if recent_is != should_be:
					# corrupt
					illegals.append(entry)
					scores.append(score[entry])
					print('found a corrupt!', entry, score[entry])
					print('current scores', scores)
					break

	return sum(scores)


def part2():
	return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
