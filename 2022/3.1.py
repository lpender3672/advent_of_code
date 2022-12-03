
lines = []
with open('2022/3.txt', 'r') as f:
    for l in f:
        lines.append(l.strip())

def priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    elif letter.islower():
        return ord(letter) - 96

score = 0
for line in lines:
    # if same letter in both halves of 
    n = len(line)
    s1 = set(line[:n//2])
    s2 = set(line[n//2:])
    if s1 & s2:
        score += sum([priority(l) for l in s1 & s2])

print(score)