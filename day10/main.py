lines = open("day10/input.txt").readlines()

adapters = [int(line.rstrip("\n")) for line in lines]

input_joltage = max(adapters) + 3

starting_joltage = 0
lowest_adapter = min(adapters)

diff_1jolt = 0
diff_3jolt = 1  # one for the jump between the highest adapter and the notebook itself

joltage = 0

while joltage != max(adapters):
    next_adapters = []
    for adapter in adapters:
        if joltage in range(adapter-3, adapter):
            next_adapters.append(adapter)
    if abs(joltage - min(next_adapters)) == 1:
        diff_1jolt += 1
    elif abs(joltage - min(next_adapters)) == 3:
        diff_3jolt += 1
    joltage = min(next_adapters)

print("result: %d" % (diff_1jolt*diff_3jolt))