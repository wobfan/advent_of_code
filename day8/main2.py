f = open("day8/input.txt", "r")
cmds = f.readlines()
splitted_cmds = []

for line in cmds:
    splitted_cmds.append(line.split(" "))
for part in splitted_cmds:
    part[1] = part[1].rstrip("\n")


    acc = 0
    fixed = False
    executed = []

    i = 0
    while i in range(0, len(splitted_cmds)+1):
        cmd = splitted_cmds[i]
        op = cmd[0]
        val = int(cmd[1])

        if fixed is not True:
            if i in executed and op == 'jmp':
                print("at #%d i would run a jmp twice now. changing it to a nop." % (i))
                op = 'nop'
                splitted_cmds[i][0] = 'nop'
                fixed = True
            executed.append(i)

        if op == "jmp":
            i = i + val
        if op == "nop":
            if i+val == len(splitted_cmds):
                print("nop at line %d should be a jmp to termination line (which is the line after the last)" % i)
            i = i + 1
        if op == "acc":
            acc = acc + val
            i = i + 1
        
        if i == len(splitted_cmds):
            print("terminateed successful. acc is %d." % acc)
            exit(0)