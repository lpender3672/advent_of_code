elves = []
with open('2022/1.txt', 'r') as f:
    elf = []
    for l in f:
        line = l.strip()
        if line == '':
            elves.append(elf)
            elf = []
        elif line.isnumeric():
            elf.append(int(line))

sums = [sum(e) for e in elves]
print(max(sums))