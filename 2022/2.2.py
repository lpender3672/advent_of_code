
round = []
with open('2022/2.txt', 'r') as f:
    for l in f:
        round.append(l.strip().split(' '))

score = 0
outcome_points = {'X': 0, 'Y': 3, 'Z': 6}

option_points = {'X': {"A" : 3, "B": 1, "C" : 2},   # loss
                 'Y': {"A" : 1, "B": 2, "C" : 3},   # draw
                 'Z': {"A" : 2, "B": 3, "C" : 1} }  # win

for r in round:
    score += outcome_points[r[1]]
    score += option_points[r[1]][r[0]]

print(score)