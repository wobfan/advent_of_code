f = open("day1/input")
lines = [l.rstrip("\n") for l in f.readlines()]
numbers = [int(l) for l in lines]

for i in numbers:
    for j in numbers:
        if i + j == 2020:
            print("the answer to the puzzle is %d" % (i*j))
            exit(0)