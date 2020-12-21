f = open("day8/input.txt", "r")
cmds = f.readlines()
splitted_cmds = []

for line in cmds:
    splitted_cmds.append(line.split(" "))
for part in splitted_cmds:
    part[1] = part[1].rstrip("\n")

original_splitted_cmds = splitted_cmds.copy()

# put all NOPs and JMPs into a list to iterate through them when changing them one after one
jmpList = []
nopList = []
for i in range(0, len(splitted_cmds)):
    if splitted_cmds[i][0] == 'jmp':
        jmpList.append(i)
    if splitted_cmds[i][0] == 'nop':
        nopList.append(i)
nextJMP = jmpList[0]
nextNOP = nopList[0]

while(True):
    if nextNOP == nopList[len(nopList)-1] and nextJMP == jmpList[len(jmpList)-1]:
        exit(0)
    elif nextJMP == jmpList[len(jmpList)-1]:
        splitted_cmds[nextNOP][0] = 'jmp'
        nextNOP += 1
    else:
        splitted_cmds[nextJMP][0] = 'nop'
        nextJMP += 1

    splitted_cmds = original_splitted_cmds.copy()
    executed = []
    acc = 0
    i = 0
    while i in range(0, len(splitted_cmds)):
        cmd = splitted_cmds[i]
        op = cmd[0]
        val = int(cmd[1])

        if i in executed:
            break
        executed.append(i)

        if op == "jmp":
            i = i + val
        if op == "nop":
            i = i + 1
        if op == "acc":
            acc = acc + val
            i = i + 1

        if i == len(splitted_cmds):
            print("terminated successfully. acc is %d." % acc)
