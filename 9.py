import numpy as np

import init

data = init.read_data(False, )


def is_lowest(i, j, heightmap):
    count = 0
    check = 0
    if i > 0:
        # check left
        check += 1
        if heightmap[i, j] - heightmap[i - 1, j] < 0:
            # current position smaller
            count += 1
    if j > 0:
        # check above
        check += 1
        if heightmap[i, j] - heightmap[i, j - 1] < 0:
            # current position smaller
            count += 1

    if i < heightmap.shape[0] - 1:
        # check right
        check += 1
        if heightmap[i, j] - heightmap[i + 1, j] < 0:
            # current position smaller
            count += 1

    if j < heightmap.shape[1] - 1:
        # check below
        check += 1
        if heightmap[i, j] - heightmap[i, j + 1] < 0:
            # current position smaller
            count += 1

    if count == check:
        return True
    else:
        return False


def part1():
    # initialise
    heightmap = np.array([np.array(list(i)) for i in data]).astype(int)
    print(heightmap)

    check = np.zeros((len(heightmap), len(heightmap[0])))

    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            # print(i, j)
            if is_lowest(i, j, heightmap):
                check[i, j] = heightmap[i, j] + 1

    return sum(sum(check))


def part2():
    return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
