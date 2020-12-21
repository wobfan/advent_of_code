lines = open("day9/input.txt").readlines()

lines = [x.rstrip("\n") for x in lines]

lines = [int(x) for x in lines]

last25 = []

def push(number):
    global last25
    last25.remove(last25[0])
    last25.append(number)

def check(number):
    for i in last25:
        for j in last25:
            if i+j == number:
                return True
    return False

for line in lines[:25]:
    last25.append(line)
lines = lines[25:]

for line in lines:
    if not check(line):
        print("%d is not a sum of one of the last 25 exchanged numbers." % line)
        exit(1)
    push(line)