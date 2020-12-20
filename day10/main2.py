lines = open("day10/input.txt").readlines()

adapters = [int(line.rstrip("\n")) for line in lines]

input_joltage = max(adapters) + 3

starting_joltage = 0
lowest_adapter = min(adapters)

joltage = 0

while joltage != max(adapters):
    next_adapters = []
    for adapter in adapters:
        if joltage in range(adapter-3, adapter):
            next_adapters.append(adapter)
    joltage = min(next_adapters)

