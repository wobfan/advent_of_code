f = open("day3/input.sql")
lines = f.readlines()

trees = 0
x = 0
line_length = len(lines[0]) - 1

for line in lines:
    line.rstrip("\n")
    if line[x] == "#":
        trees += 1
    x += 3
    x = x % line_length

print(trees)