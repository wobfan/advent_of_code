f = open("day3/input.sql")
lines = f.readlines()

trees = 1
x = 0
line_length = len(lines[0]) - 1

slopes = [[1,3,5,7,1], [1,1,1,1,2]]

for i in range(0,5):
    right = slopes[0][i]
    down = slopes[1][i]
    j = 0
    current_trees = 0
    while j in range(0, len(lines)):
        lines[j].rstrip("\n")
        if lines[j][x] == "#":
            current_trees += 1
        x += right
        x = x % line_length
        j += down
    x = 0
    trees *= current_trees

print(trees)