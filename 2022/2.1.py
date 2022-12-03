
round = []
with open('2022/2.txt', 'r') as f:
    for l in f:
        round.append(l.strip().split(' '))

score = 0
option_points = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
for r in round:
    score += option_points[r[1]] + 1
    if (option_points[r[0]] + 1) % 3 == option_points[r[1]]:
        score += 6
    elif option_points[r[0]] == option_points[r[1]]:
        score += 3
    
print(score)