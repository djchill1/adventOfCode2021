import init

data = init.read_data(False,)


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


def delete_from_list(input, value, bit):
	result = []
	for entry in input:
		# print(entry)
		entry = str(entry)
		if entry[bit] == str(value):
			result.append(entry)

	return result


def list_reducer(input, most = True):
	byte_length = len(input[0])
	if most:
		round_up = True
	else:
		round_up = False

	bit = 0
	while True:

		number_of_values = len(input)
		count = 0

		print('checking bit', bit, 'for input', input)

		# check if last element
		if number_of_values == 1:
			return input[0]

		# find how many 1s
		for i in input:
			# ith element value
			if str(i)[bit] == '1':
				count += 1
			print(i, count)

		if count / number_of_values > 0.5:
			if round_up:
				# 1 wins
				input = delete_from_list(input, 1, bit)
				print('1 wins')
			else:
				# 0 wins
				input = delete_from_list(input, 0, bit)
				print('0 wins')
		elif count / number_of_values < 0.5:
			if round_up:
				# 0 wins
				input = delete_from_list(input, 0, bit)
				print('0 wins')
			else:
				# 1 wins
				input = delete_from_list(input, 1, bit)
				print('1 wins')
		else:
			# round correctly
			if round_up:
				input = delete_from_list(input, 1, bit)
				print('1 wins')
			else:
				input = delete_from_list(input, 0, bit)
				print('0 wins')

		bit += 1




def part2():
	oxy_possibles = data


	oxygen = list_reducer(data, True)
	print('CO2 NOW *******************************************')
	co2 = list_reducer(data, False)

	oxygen = int(oxygen, 2)
	co2 = int(co2, 2)

	return int(oxygen) * int(co2)


print(f'Part 1: {part1()}, Part 2: {part2()}')