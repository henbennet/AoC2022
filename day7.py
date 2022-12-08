import re
import aocMain
from collections import defaultdict

def ParseDirectory(index, inputlines):
    size = 0



    return size
def Move1(par):
    return 0

def Move2(par):
    return 0

def main(inputlines):
    SZ = defaultdict(int)
    path = []
    for line in inputlines:
        words = line.strip().split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            size = int(words[0])
            # Add this file's size to the current directory size *and* the size of all parents
            for i in range(1, len(path) + 1):
                SZ['/'.join(path[:i])] += size

    max_used = 70000000 - 30000000
    total_used = SZ['/']
    need_to_free = total_used - max_used

    p1 = 0
    p2 = 1e9
    for k, v in SZ.items():
        # print(k,v)
        if v <= 100000:
            p1 += v
        if v >= need_to_free:
            p2 = min(p2, v)

    return p1, p2

aocMain.runLines(main, "day7.txt")
