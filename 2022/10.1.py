
instructions = []
with open('2022/10.txt', 'r') as f:
    for l in f:
        instructions.append(l.strip().split(' '))


val = 0
cycles = 0
important_cycles = [20, 60, 100, 140, 180, 220]
answer = 0
for line in instructions:
    if line[0] == 'noop':
        cycles += 1
        
    elif line[0] == 'addx':
        cycles += 2
        val += int(line[1])
        print(val)
    
    if cycles in important_cycles:
        answer += cycles*val

print(answer)