import init

data = init.read_data(True, )


def part1(maximum):
    polymer_template = list(data[0])
    pair_rules = []

    for line in [list(map(str, x.split())) for x in data[2::]]:
        appender = [line[0][0], line[0][1], line[2]]
        pair_rules.append(appender)

    # print(polymer_template)
    # print(pair_rules)

    count = 0
    while count < maximum:
        new_polymer_template = []
        polymer_counts = {}
        for index, value in enumerate(polymer_template):
            # print(index, value)
            new_polymer_template.append(value)
            if value not in polymer_counts:
                polymer_counts[value] = 1
            else:
                polymer_counts[value] += 1

            if index == len(polymer_template) - 1:
                # end value
                break

            next_value = polymer_template[index + 1]
            # print('checking between', value, next_value)
            for line in pair_rules:
                if (value, next_value) == (line[0], line[1]):
                    # print('adding in', line[2])
                    new_polymer_template.append(line[2])
                    if line[2] not in polymer_counts:
                        polymer_counts[line[2]] = 1
                    else:
                        polymer_counts[line[2]] += 1

        count += 1
        polymer_template = new_polymer_template
        # print(polymer_template)
        # print(polymer_counts)

    all_values = polymer_counts.values()
    max_value = max(all_values)
    min_value = min(all_values)
    print('part 1', polymer_counts)
    return max_value - min_value


def add_to_dict(dictionary, key, value=1):
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += value
    return dictionary


def part2(maximum):
    polymer_template = list(data[0])
    pair_rules = []

    for line in [list(map(str, x.split())) for x in data[2::]]:
        appender = [line[0][0], line[0][1], line[2]]
        pair_rules.append(appender)

    polymer_pair_counts = {}

    # initalise the pair counts
    for index, value in enumerate(polymer_template):
        if index == len(polymer_template) - 1:
            # end value
            break

        next_value = polymer_template[index + 1]

        pair = value + next_value

        if pair not in polymer_pair_counts:
            polymer_pair_counts[pair] = 1
        else:
            polymer_pair_counts[pair] += 1

    print(polymer_pair_counts)

    count = 0
    while count < maximum:
        new_polymer_pair_counts = {}
        for (key, value) in polymer_pair_counts.items():
            # print(key, value)

            for line in pair_rules:
                # print('checking', line[0] + line[1])
                if key == line[0] + line[1]:
                    new_pair = line[0] + line[2]
                    print(key, 'is a MATCH! Adding in', new_pair)
                    new_polymer_pair_counts = add_to_dict(new_polymer_pair_counts, new_pair)
                    new_pair = line[2] + line[1]
                    print('also adding in', new_pair)
                    new_polymer_pair_counts = add_to_dict(new_polymer_pair_counts, new_pair)
                    break

        polymer_pair_counts = new_polymer_pair_counts
        print(polymer_pair_counts)
        count += 1

    # pairs to values
    letters = {}
    for letter1, letter2 in polymer_pair_counts:
        value = polymer_pair_counts[letter1 + letter2]
        print(letter1, letter2, value)
        letters = add_to_dict(letters, letter1, value)
        letters = add_to_dict(letters, letter2, value)

    all_values = letters.values()
    print(letters)
    max_value = max(all_values)
    min_value = min(all_values)
    return max_value - min_value
    # return False


n = 3
print(f'Part 1: {part1(n)}, Part 2: {part2(n)}')
