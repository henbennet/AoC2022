import re
import aocMain

def GetCrates(inputlines):
    #print("get grates")
    pat_digit = r'd+'
    pat_crates = r'[A-Z]'
    crates = [[]]
    for line in inputlines:
        for index, c in enumerate(line):
            if re.search(pat_crates, c) is not None:
                spot = int((index-1)/4)
                while len(crates) < spot+1:
                    crates.append([])

                crates[spot].insert(0, c)

        if re.search(pat_digit, line) is not None:
            return crates
    return crates

def Move(no, fr, to, crates):
    for i in range(no):
        crate = crates[fr-1].pop()
        crates[to-1].append(crate)
    return crates


def MovePart2(no, fr, to, crates):
    move = []
    for i in range(no):
        crate = crates[fr - 1].pop()
        move.insert(0, crate)

    for c in move:
        crates[to-1].append(c)
    return crates

def main(inputlines):
    crates = GetCrates(inputlines)
    pattern = r'move*'
    pat_dig = r'\d+'
    for line in inputlines:
        if re.search(pattern, line) is not None:
            inst = re.findall(pat_dig, line)
            crates = Move(int(inst[0]), int(inst[1]), int(inst[2]), crates)
    top = ""
    for crate in crates:
        if len(crate)-1 >= 0:
            top += crate[len(crate)-1]



    part1 = top

    crates = GetCrates(inputlines)
    pattern = r'move*'
    pat_dig = r'\d+'
    for line in inputlines:
        if re.search(pattern, line) is not None:
            inst = re.findall(pat_dig, line)
            crates = MovePart2(int(inst[0]), int(inst[1]), int(inst[2]), crates)
    top = ""
    for crate in crates:
        if len(crate) - 1 >= 0:
            top += crate[len(crate) - 1]

    part2 = top

    return part1, part2

aocMain.runLines(main, "day5.txt")
