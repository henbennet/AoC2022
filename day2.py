import aocMain

def main(inputlines):

    base = 87

    sum = 0

    for line in inputlines:
            a1 = int(ord(line[0]))
            a2 = int(ord(line[2]))
            sum += (a2-base)
            result = a2-a1

            if result == 23:
                sum += 3
            elif result == 21 or result == 24:
                sum += 6


    part1 = sum
    opbase = 64
    sum = 0
    for line in inputlines:
        a1 = int(ord(line[0]))
        a2 = int(ord(line[2]))

        if a2 == 88: #förlust
            if a1 == 65:
                a2 = a1 + 25
            else:
                a2 = a1 + 22
            sum += a2 - base

        elif a2 == 89: #lika
            sum += 3
            a2 = a1 + 23
            sum += a2 - base

        elif a2 == 90: #vinst
            sum += 6
            if a1 == 67:
                a2 = a1 + 21
            else:
                a2 = a1 + 24
            sum += a2 - base


    part2 = sum

    return part1, part2

aocMain.runLines(main, "day2.txt")
