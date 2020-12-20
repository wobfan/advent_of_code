lines = open("day9/input.txt").readlines()

lines = [x.rstrip("\n") for x in lines]

lines = [int(x) for x in lines]

last25 = []

wrong_number = 0

def get_summands(number):
    global lines
    summands = []
    for i in range(0,len(lines)):
        test = lines[i]
        summands.append(test)
        for j in range(i+1,len(lines)):
            if test > number:
                continue
            test += lines[j]
            summands.append(lines[j])
            if test == number:
                return summands
        summands = []

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
        wrong_number = line
        break
    push(line)

summands = get_summands(wrong_number)

print(f"encryption weakness for {wrong_number} is {max(summands)+min(summands)}")