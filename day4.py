import re
import aocMain

def Part2(group):
    print("part2")
    return 0

def main(inputlines):
    count = count2 = 0
    pattern = r'\d+'
    for line in inputlines:
        s1, e1, s2, e2 = [int(x) for x in re.findall(pattern, line)]
        if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
            count += 1
        if not (e1 < s2 or s1 > e2):
            count2 += 1

    part1 = count

    part2 = count2

    return part1, part2

aocMain.runLines(main, "day4.txt")
