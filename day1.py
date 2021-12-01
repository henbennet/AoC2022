import aocMain


def main(inputlines):
    values = [int(val) for val in inputlines]
    part1 = 0
    part2 = 0

    for i, dist in enumerate(values):
        if dist > values[i - 1]:
            part1 += 1

    prev = 0
    for i, dist in enumerate(values):
        if i - 2 >= 0:
            current = dist + values[i - 1] + values[i - 2]
            if 0 < prev < current:
                part2 += 1
            prev = current

    return part1, part2


aocMain.runLines(main, "day1.txt")
