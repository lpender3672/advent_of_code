
line = ""
with open('2022/6.txt', 'r') as f:
    for l in f:
        line = l.strip()

for i, l in enumerate(line):
    if len(set(line[i:i+14])) == 14:
        print(i+14)
        break
