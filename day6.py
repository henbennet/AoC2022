import re
import aocMain

def Parse(inputlines):
    return 0
def Move1(par):
    return 0

def Move2(par):
    return 0

def main(inputlines):
    pattern = r'\d+'
    count = 0
    for line in inputlines:
        received = ""
        count = 0
        for index, c in enumerate(line):
            count += 1
            if index > 3:
                lastfour = line[index-4:index]
                found = True
                for l in lastfour:
                    if lastfour.count(l) > 1:
                        found = False

                if found:
                    part1 = index
                    #print(lastfour)
                    break

            #if received.count(c) <=0:
            #    received += c

            #if len(received) >= 4:
            #    print(received)
            #    break

#    part1 = count
    count = 0
#    for line in inputlines:
#        received = []
#        for index, c in enumerate(line):
#            if len(received) >= 14:
#                print(received)
#                part2 = index + 1
#                break
#            if received.count(c) <= 0:
#                received.append(c)

    #lines = [x for x in data.split('\n')]

    p1 = False
    p2 = False
    for line in inputlines:
        for i in range(len(line)):
            if (not p1) and i - 3 >= 0 and len(set([line[i - j] for j in range(4)])) == 4:
                print(i + 1)
                p1 = True
            if (not p2) and i - 13 >= 0 and len(set([line[i - j] for j in range(14)])) == 14:
                print(i + 1)
                p2 = True

    return part1, 0

aocMain.runLines(main, "day6.txt")
