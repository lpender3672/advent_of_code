
pairs = []
with open('2022/4.txt', 'r') as f:
    for l in f:
        pairs.append(l.strip())

score = 0
for pair in pairs:
    range1,range2 = pair.split(',')
    low1,high1 = range1.split('-')
    low1,high1 = int(low1),int(high1)
    low2,high2 = range2.split('-')
    low2,high2 = int(low2),int(high2)

    if (low1 <= low2 and high2 <= high1) or (low2 <= low1 and high1 <= high2):
        score += 1

print(score)