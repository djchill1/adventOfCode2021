import numpy as np

import init

data = init.read_data(True, )


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


def floodfill(heightmap, i, j, size):
    target = heightmap[i][j]
    if target == 9:
        return heightmap
    size.append(target)
    print('floodfilling', i, j)
    if i > 0:
        print('checking left', i - 1, j)
        floodfill(heightmap, i - 1, j, size)
    if i < heightmap.shape[0] - 1:
        print('checking right', i + 1, j)
        floodfill(heightmap, i + 1, j, size)
    if j > 0:
        floodfill(heightmap, i, j - 1, size)
    if j < heightmap.shape[1] - 1:
        floodfill(heightmap, i, j + 1, size)

    # if i > 0:
    #     # check left
    #     if heightmap[i, j] - heightmap[i - 1, j] == 1:
    #         # exactly one size up
    #         size += 1
    #         heightmap[i, j] = 99
    # if j > 0:
    #     # check above
    #     if heightmap[i, j] - heightmap[i, j - 1] == 1:
    #         # exactly one size up
    #
    # if i < heightmap.shape[0] - 1:
    #     # check right
    #     if heightmap[i, j] - heightmap[i + 1, j] == 1:
    #         # exactly one size up
    #
    # if j < heightmap.shape[1] - 1:
    #     # check below
    #     if heightmap[i, j] - heightmap[i, j + 1] == 1:
    #         # exactly one size up

    return heightmap, size


def part1():
    # initialise
    heightmap = np.array([np.array(list(i)) for i in data]).astype(int)
    # print(heightmap)

    check = np.zeros((len(heightmap), len(heightmap[0])))

    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            # print(i, j)
            if is_lowest(i, j, heightmap):
                check[i, j] = heightmap[i, j] + 1

    return sum(sum(check))


def part2():
    # initialise
    heightmap = np.array([np.array(list(i)) for i in data]).astype(int)
    # print(heightmap)

    minimums = np.zeros((len(heightmap), len(heightmap[0]))).astype(int)

    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            # print(i, j)
            if is_lowest(i, j, heightmap):
                minimums[i, j] = 1

    # flood fill up from minimums
    sizes = []
    size = []
    print(heightmap)
    print(minimums)
    for j in range(heightmap.shape[0]):
        for i in range(heightmap.shape[1]):
            if minimums[j][i] == 1:
                print('starting floodfill on', i, j)
                # start the floodfill
                heightmap, size = floodfill(heightmap, i, j, size)
                # append size of fill to sizes
                if size:
                    sizes.append(size)
                    size = []

    print(sizes)

    return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
