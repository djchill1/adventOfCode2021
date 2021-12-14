import init

data = init.read_data(False, )


def part1(maximum):
    polymer_template = list(data[0])
    pair_rules = []

    for line in [list(map(str, x.split())) for x in data[2::]]:
        appender = [line[0][0], line[0][1], line[2]]
        pair_rules.append(appender)

    print(polymer_template)
    print(pair_rules)

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
    return max_value - min_value


def part2():
    return False


print(f'Part 1: {part1(40)}, Part 2: {part2()}')
