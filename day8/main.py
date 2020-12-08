f = open("advent_of_code/day8/input.txt", "r")
cmds = f.readlines()
splitted_cmds = []

for line in cmds:
    splitted_cmds.append(line.split(" "))
for part in splitted_cmds:
    part[1] = part[1].rstrip("\n")

acc = 5

executed = []

i = 0
while i in range(0, len(splitted_cmds)):
    cmd = splitted_cmds[i]
    op = cmd[0]
    val = int(cmd[1])

    if "%s %d" % (op, val) in executed:
        print("would run instruction '%s %d' twice now. accumulator is %d." % (op, val, acc))
        exit(0)
    executed.append("%s %d" % (op, val))

    if op == "jmp":
        i = i + val
    if op == "nop":
        i = i + 1
    if op == "acc":
        acc = acc + val
        i = i + 1