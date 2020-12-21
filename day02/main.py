f = open("day2/input.sql")
lines = f.readlines()

def count_char(string, char):
    cnt = 0
    for i in range(0,len(string)):
        if char == string[i]:
            cnt += 1
    return cnt

correct_idx = 0
incorrect_idx = 0

for line in lines:
    parts = line.split(' ')
    minmax = parts[0].split("-")
    min = int(minmax[0])
    max = int(minmax[1])
    char = parts[1].rstrip(":")
    password = parts[2].rstrip("\n")

    if min <= count_char(password, char) <= max:
        correct_idx += 1
    else:
        incorrect_idx += 1

print("%d were correct, while %d were incorrect." % (correct_idx, incorrect_idx))