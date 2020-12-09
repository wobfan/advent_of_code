f = open("day1/input")
lines = [l.rstrip("\n") for l in f.readlines()]
numbers = [int(l) for l in lines]

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print("the answer to the puzzle is %d" % (i*j*k))
                exit(0)