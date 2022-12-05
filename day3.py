import aocMain
def Part2(group):
    for a in group[0]:
        for b in group[1]:
            if a == b:
                for c in group[2]:
                    if a == c:
                        return int(ord(a))
    return 0

def Prio(item):
    if item >= 97:
        return item - 96
    else:
        return item - 65 + 27

def main(inputlines):


    sum = 0
    sum2 = 0
    counter = 0
    group = []
    for line in inputlines:
        length = len(line)
        first = line[:int(length/2)]
        snd = line[int(length/2):length-1]
        prio = []
        for c in first:
            for d in snd:
                if c == d:
                    if not any(c for x in prio):
                        prio.append(c)

        for c in prio:
            val = int(ord(c))
            sum += Prio(val)

        counter += 1
        group.append(line)

        if counter >= 3:
            val = Part2(group)
            sum2 += Prio(val)
            group.clear()
            counter = 0

    part1 = sum

    part2 = sum2
    return part1, part2

aocMain.runLines(main, "day3.txt")
