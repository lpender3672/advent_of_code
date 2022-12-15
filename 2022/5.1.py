
lines = []
with open('2022/5.txt', 'r') as f:
    for l in f:
        lines.append(l.strip("\n"))

# seperate into stacks and moves
split = lines.index('')
collumns, instructions = lines[:split-1], lines[split+1:]

num, to, fro = [],[],[]

for i in instructions:
    instr = i.split(' ')
    num.append(int(instr[1]))
    fro.append(int(instr[3]) - 1)
    to.append(int(instr[5]) - 1)

letters = []
max_len = max(len(item[1::4]) for item in collumns)

for i,collumn in enumerate(collumns):
    c = list(collumns[i][1::4])
    while len(c) < max_len:
        c.append(' ')
    letters.append(c)

stacks = list(zip(*letters[::-1]))
stacks = [[l for l in s if l != ' '] for s in stacks]

for n, f, t in zip(num, fro, to):
    for i in range(n):
        # add last to to
        # remove last from fro
        stacks[t] += stacks[f][-1:]
        stacks[f] = stacks[f][:-1]

result = ""
for s in stacks:
    result += s[-1]

print(result)
