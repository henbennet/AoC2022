import time

def runLines(mainFunction, day):
    with open("input/" + day) as file:
        rawInput = file.readlines()
    run(mainFunction, rawInput)


def run(mainFunction, rawInput):
    start = time.time()
    part1, part2 = mainFunction(rawInput)
    print("Executed time: ", time.time() - start, " ms")
    print("part1: ", part1)
    print("part2: ", part2)

