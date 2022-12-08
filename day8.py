import re
import aocMain
def parseMap(inputLines):
    map = []
    for line in inputLines:
        map.append(line.strip())
    return map

def calcSS(input, i, j):
    current = int(input[i][j])
    ss = 1
    count=0
    # i->0
    for r in range(i-1, 0-1, -1):
        count += 1
        if int(input[r][j]) >= current:
            break;
    ss *= count
    # i->end
    count = 0
    for r in range(i+1, len(input)):
        count += 1
        if int(input[r][j]) >= current:
            break
    ss *= count
    # j->0
    count = 0
    for c in range(j-1, 0-1, -1):
        count += 1
        if int(input[i][c]) >= current:
            break
    ss *= count
    # j->end
    count = 0
    for c in range(j+1, len(input[i])):
        count += 1
        if int(input[i][c]) >= current:
            break
    ss *= count
    return ss

def isVisible(input, i, j):
    if i == 0 or i >= len(input)-1 or j == 0 or j >= len(input[i])-1:
        return True

    vissible = False
    current = int(input[i][j])
    # 0 -> i-1 | top to tree
    for r in range(0, i+1):
        if r == i:
            return True
        if int(input[r][j]) >= current:
            break

    #end -> i
    for r in range(len(input)-1, i-1, -1):
        if r == i:
            return True
        if int(input[r][j]) >= current:
            break

    #0 -> j
    for c in range(0, j+1):
        if c == j:
            return True
        if int(input[i][c]) >= current:
            break

    #end -> j
    for c in range(len(input[i])-1, j-1, -1):
        if c == j:
            return True
        if int(input[i][c]) >= current:
            break


    return False

def Move2(par):
    return 0

def main(inputlines):

    map = parseMap(inputlines) #tree map

    vissible = 0
    p1 = p2 = 0
    ss = 0
    for i, line in enumerate(map):
        for j, tree in enumerate(line):
            #print(tree)
            if isVisible(map, i, j):
                vissible += 1
                #print("T", end="")
    #        else:
                #print("F", end="")
            s = calcSS(map, i, j)
            if s > ss:
                ss = s
        #print()
    p1 = vissible
    p2 = ss
    return p1, p2

aocMain.runLines(main, "day8.txt")
