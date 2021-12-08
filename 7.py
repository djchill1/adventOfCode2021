import init

data = init.read_data(False, 'intlist')


def part1():
    start = min(data)
    end = max(data)
    current_best = []

    for pos in range(start, end + 1):
        cost = 0
        for ship in data:
            cost += abs(pos - ship)
        if current_best == [] or cost < current_best[1]:
            current_best = (pos, cost)

    return current_best


def part2():
    start = min(data)
    end = max(data)
    current_best = []
    for pos in range(start, end + 1):
        cost = 0
        for ship in data:
            ship_cost = 0
            displacement = abs(pos - ship)
            ship_cost = ((displacement) * (displacement + 1)) / 2
            # print(ship, ship_cost)
            cost += ship_cost
        if current_best == [] or cost < current_best[1]:
            current_best = (pos, cost)
    # print(pos, cost)
    return current_best


print(f'Part 1: {part1()}, Part 2: {part2()}')
