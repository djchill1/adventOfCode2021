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
    # heightmap = np.array([np.array(list(i)) for i in data]).astype(int)
    # print(heightmap)

    heightmap = [[0 if num != "9" else 9 for num in line.strip()] for line in data]
    width = len(heightmap[0])
    height = len(heightmap)

    def floodfill(matrix, x, y):
        score = 0
        if matrix[y][x] == 0:
            matrix[y][x] = 1
            score = 1
            if x > 0:
                score += floodfill(matrix, x - 1, y)
            if x < len(matrix[0]) - 1:
                score += floodfill(matrix, x + 1, y)
            if y > 0:
                score += floodfill(matrix, x, y - 1)
            if y < len(matrix) - 1:
                score += floodfill(matrix, x, y + 1)
        return score

    scores = []
    for idx in range(width):
        for jdx in range(height):
            scores.append(floodfill(heightmap, idx, jdx))

    scores = sorted(scores, reverse=True)[:3]

    return (scores[0] * scores[1] * scores[2])


print(f'Part 1: {part1()}, Part 2: {part2()}')
