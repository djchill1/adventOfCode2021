import init

data = init.read_data(False, )


def filter_corrupts(data):
	closing_braces = {')': '(', ']': '[', '}': '{', '>': '<'}
	open_braces = {'(': 0, '[': 0, '{': 0, '<': 0}

	score = {')': 3, ']': 57, '}': 1197, '>': 25137}
	scores = []
	illegals = []
	corrupt = []

	for line in data:
		# print(line)
		chunks = []
		for entry in line:
			# print(entry)
			if entry in open_braces:
				chunks.append(entry)
			elif entry in closing_braces:
				# what should the most recent chunk be:
				should_be = closing_braces[entry]
				recent_is = chunks.pop(-1)
				if recent_is != should_be:
					corrupt.append(line)
					# corrupt
					illegals.append(entry)
					scores.append(score[entry])
					# print('found a corrupt!', entry, score[entry])
					# print('current scores', scores)
					break

	return scores, corrupt


def part1():
	scores, corrupt = filter_corrupts(data)
	return sum(scores)


def part2():
	closing_braces = {')': '(', ']': '[', '}': '{', '>': '<'}
	closing_braces_reversed = {'(': ')', '[': ']', '{': '}', '<': '>'}
	open_braces = {'(': 0, '[': 0, '{': 0, '<': 0}

	valid_scores, corrupt = filter_corrupts(data)
	incompletes = []
	for line in data:
		if line not in corrupt:
			incompletes.append(line)
	print(incompletes)

	score = {')': 1, ']': 2, '}': 3, '>': 4}
	scores = []

	for line in incompletes:
		total_score = 0
		to_append = []
		# print(line)
		chunks = []
		for entry in line:
			# print(entry)
			if entry in open_braces:
				chunks.append(entry)
			elif entry in closing_braces:
				# can safely remove last as we know chunk is valid.
				chunks.pop(-1)
		# whats left needs matching.
		print(chunks)
		for opener in reversed(chunks):
			closer = closing_braces_reversed[opener]
			total_score *= 5
			total_score += score[closer]
		print('to append', to_append, total_score)
		scores.append(total_score)
	print(sorted(scores))
	answer = sorted(scores)
	middle_val = int((len(scores) - 1) / 2)
	return answer[middle_val]


print(f'Part 1: {part1()}, Part 2: {part2()}')
