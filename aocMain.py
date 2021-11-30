import time

def parseLines(mainFunction, day):
    with open("input/" + day) as file:
        rawInput = file.readlines()
    run(mainFunction, rawInput)


def run(mainFunction, rawInput):
    start = time.time()
    mainFunction(rawInput)
    print("Executed time: ", time.time() - start, " ms")
    print("part1: ")
    print("part2: ")

