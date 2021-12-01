import init

data = init.read_data(False, 'int')

def part_1(data):
    counter = 0
    prev_number = data[0]

    for number in data:
        if number > prev_number:
            counter += 1
        #     print(number, 'larger', counter)
        # elif number < prev_number:
        #     print(number, 'smaller')
        # else:
        #     print(number, 'n/a')

        prev_number = number

    print(counter)


def part_2(data):
    sums = []
    for index, elem in enumerate(data):
        try:
            sum = elem + data[index+1] + data[index+2]
            sums.append(sum)
        except:
            pass
    # for sum in sums:
        # print(sum)

    part_1(sums)

part_2(data)