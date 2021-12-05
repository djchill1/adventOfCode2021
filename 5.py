import re

import numpy as np

import init

data = init.read_data(False, )


def part1():
    # initalise
    values = []
    largest = 0
    for line in data:
        vals = re.split(' |,', line)
        interim = [int(vals[0]), int(vals[1]), int(vals[3]), int(vals[4])]
        if interim[0] > interim[2] or interim[1] > interim[3]:
            # rotate order if end is smaller
            interim = [int(vals[3]), int(vals[4]), int(vals[0]), int(vals[1])]
        values.append(interim)
        for value in interim:
            if value > largest:
                largest = value

    counts = np.zeros((largest + 1, largest + 1))

    # counts[1,7] = 4

    # add to counts
    for instruction in values:
        x1, y1, x2, y2 = instruction
        if x1 == x2 or y1 == y2:
            # print('valid range', x1, y1, x2, y2)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    # print('(x,y)=',x,y)
                    counts[y, x] += 1

    # print(counts)

    danger_count = 0
    for row in counts:
        for element in row:
            # print(element)
            if element >= 2:
                danger_count += 1
    return danger_count


def part2():
    # initalise
    values = []
    largest = 0
    for line in data:
        vals = re.split(' |,', line)
        interim = [int(vals[0]), int(vals[1]), int(vals[3]), int(vals[4])]
        if interim[0] > interim[2] or interim[1] > interim[3]:
            # rotate order if end is smaller
            interim = [int(vals[3]), int(vals[4]), int(vals[0]), int(vals[1])]
        values.append(interim)
        for value in interim:
            if value > largest:
                largest = value

    counts = np.zeros((largest + 1, largest + 1))

    # counts[1,7] = 4

    # add to counts
    for instruction in values:
        x1, y1, x2, y2 = instruction
        if x1 == x2 or y1 == y2:
            print('vert/horiz', x1, y1, x2, y2)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    # print('(x,y)=', x, y)
                    counts[y, x] += 1

        elif (x1 < x2) & (y1 < y2):
            points = [(x1 + i, y1 + i) for i in range(x2 - x1 + 1)]
            for x, y in points:
                counts[y, x] += 1
        elif (x1 < x2) & (y1 > y2):
            points = [(x1 + i, y1 - i) for i in range(x2 - x1 + 1)]
            for x, y in points:
                counts[y, x] += 1
        elif (x1 > x2) & (y1 > y2):
            points = [(x1 - i, y1 - i) for i in range(x1 - x2 + 1)]
            for x, y in points:
                counts[y, x] += 1
        elif (x1 > x2) & (y1 < y2):
            points = [(x1 - i, y1 + i) for i in range(x1 - x2 + 1)]
            for x, y in points:
                counts[y, x] += 1

    print(counts)

    danger_count = 0
    for row in counts:
        for element in row:
            # print(element)
            if element >= 2:
                danger_count += 1
    return danger_count


print(f'Part 1: {part1()}, Part 2: {part2()}')
