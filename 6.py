import init


# new fish need +2 days.
# fish created every 7 days (AFTER 0).
# when created, parent resets to 6.

def part1(dayLim):
    data = init.read_data(True, 'intlist')
    day = 0
    while day < dayLim:
        create = 0
        for index, entry in enumerate(data):
            # print(entry, index)
            if entry == 0:
                create += 1
                data[index] = 6
            else:
                data[index] = entry - 1

        # create new fish
        for x in range(0, create):
            data.append(8)

        day += 1

    # print('after', day, 'days: ', data)
    return len(data)


def part2(dayLim):
    data = init.read_data(False, 'intlist')
    day = 0

    data_dict = {}
    data_dict["6_new"] = 0

    for i in range(9):
        data_dict[i] = 0

    for fish in data:
        data_dict[fish] += 1

    while day < dayLim:

        new_dict = {}
        new_dict[6] = data_dict[0]
        new_dict['6_new'] = data_dict[7]
        new_dict[5] = data_dict[6] + data_dict['6_new']

        for i in [1, 2, 3, 4, 5, 8]:
            new_dict[i - 1] = data_dict[i]

        new_dict[8] = new_dict[6]

        data_dict = new_dict

        day += 1
        print('after', day, 'days: ', data_dict)
    return sum(data_dict.values())


print(f'Part 1: {part1(80)}, Part 2: {part2(256)}')
