
groups = []
group = []
with open('2022/3.txt', 'r') as f:
    for i,l in enumerate(f):
        group.append(l.strip())
        if i % 3 == 2:
            groups.append(group)
            group = []
            
def priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    elif letter.islower():
        return ord(letter) - 96

score = 0
for group in groups:
    sets = [set(l) for l in group]
    common = sets[0] & sets[1] & sets[2]
    score += sum([priority(l) for l in common])

print(score)