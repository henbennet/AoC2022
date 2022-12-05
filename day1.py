import aocMain

def main(inputlines):
    elfs = []
    for elf in (''.join(inputlines)).split('\n\n'):
        elfC = 0
        for c in elf.split('\n'):
            elfC += int(c)
        elfs.append(elfC)
    elfs.sort()

    part1 = elfs[-1]
    part2 = elfs[-1]+elfs[-2]+elfs[-3]

    return part1, part2

aocMain.runLines(main, "day1.txt")
