import init

data = init.read_data(True,)


def sums(data):
	max = len(data[0])
	count = len(data)
	interim = []
	checker = []
	for i in range(0, max):
		interim.append(0)
		checker.append(count / 2)
	for number in data:
		for index, elem in enumerate(number):
			# print(interim)
			# print(elem)
			interim[index] += int(elem)
	return interim, checker



def part1():
	max = len(data[0])
	count = len(data)
	interim = []
	checker = []
	for i in range(0, max):
		interim.append(0)
		checker.append(count/2)
	for number in data:
		for index, elem in enumerate(number):
			# print(interim)
			# print(elem)
			interim[index] += int(elem)

	# print(interim)

	gamma = ''
	epsilon = ''

	# setup checking array to decide if 1 or 0 in final output:
	for index, elem in enumerate(interim):
		if elem > checker[index]:
			gamma = gamma + '1'
			epsilon = epsilon + '0'
		else:
			gamma = gamma + '0'
			epsilon = epsilon + '1'
	print(gamma, epsilon)

	gamma = int(gamma, 2)
	epsilon = int(epsilon, 2)

	print(gamma, epsilon)


	return gamma * epsilon


def part2():
	max = len(data[0])

	most = data
	least = data

	# oxygen
	for i in range(0, max):
		interim, checker = sums(most)

		for index, elem in enumerate(interim):
			if elem >= checker[index]:
				# most common element is 1:
				comm = 1
			else:
				comm = 0

		new_most = []
		for number in most:
			if number[i] == comm:
				new_most.append(number)
		most = new_most
	print(most)

	# return oxygen * co2


print(f'Part 1: {part1()}, Part 2: {part2()}')