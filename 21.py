import init
import re

data = init.read_data(True, )

starts = []
for line in data:
	_, start = re.split(": ", line)
	starts.append(int(start))


def play_dice(scores, pos, die_current, die_sides, total_rolls, winning_score):
	for index, pawn_location in enumerate(pos):
		dice_total = 0
		die_values = []
		# roll the dice and sum the 3 rolls
		for i in range(0, 3):
			dice_total += die_current
			die_values.append(die_current)
			die_current += 1
			die_current = die_current % die_sides
			total_rolls += 1
			if die_current == 0:
				die_current = die_sides

		# add sum of rolls to pos.
		pawn_location += dice_total

		# modulo 10 the result, this is the new position. (note 0 = 10)
		pawn_location = pawn_location % 10
		if pawn_location == 0:
			pawn_location = 10

		pos[index] = pawn_location

		# add new position to score.
		scores[index] += pawn_location
		print('player', index + 1, 'rolls a', die_values, 'and moves to space', pawn_location, 'for a total score of',
			  scores[index])

		# check if winner
		if scores[index] >= winning_score:
			break

	return scores, pos, die_current, die_sides, total_rolls, index


def part1(starts, die_sides, winning_score):
	scores = [0, 0]
	pos = starts
	die_current = 1
	total_rolls = 0
	while True:
		scores, pos, die_current, die_sides, total_rolls, index = play_dice(scores, pos, die_current, die_sides,
																			total_rolls, winning_score)

		# check if winner
		if scores[index] >= winning_score:
			break

	# repeat for next pawn
	if index == 0:
		losing_player = 1
	else:
		losing_player = 0
	losing_score = scores[losing_player]
	answer = losing_score * total_rolls

	return answer


def part2(starts, die_sides, winning_score):
	scores = [0, 0]
	pos = starts
	die_current = 1
	winning_games = [0, 0]

	while True:
		scores, pos, die_current, die_sides, total_rolls, index = play_dice(scores, pos, die_current, die_sides,
																			total_rolls, winning_score)

		# check if winner
		if scores[index] >= winning_score:
			winning_games[index] += 1
			break


	return False


print(f'Part 1: {part1(starts, 100, 1000)}, Part 2: {part2(starts, 3, 21)}')
