moves = []
with open('2022/9.txt', 'r') as f:
    for l in f:
        moves.append(l.strip().split(' '))

for m in moves:
    m[1] = int(m[1])

# start
head = (0, 0)
tail = (0, 0)
visited = [tail]

def get_direction(d):
    if d == 'U':
        return [0, 1]
    elif d == 'D':
        return [0, -1]
    elif d == 'R':
        return [1, 0]
    elif d == 'L':
        return [-1, 0]

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

head = (0, 0)
tail = (0, 0)
visited = set()
element = [(0,0) for _ in range(10)]
visited.add(element[0])

def move(head, tail, d):
    dx, dy = head[0] - tail[0], head[1] - tail[1]
    if abs(dx) > 1 or abs(dy) > 1:
        tail = (tail[0] + sign(dx), tail[1] + sign(dy))
    return tail

for direction, steps in moves:
    for _ in range(int(steps)):
        d = get_direction(direction)
        element[0] = (element[0][0] + d[0], element[0][1] + d[1])
        head = element[0]
        for i in range(1, len(element)):
            element[i] = move(element[i-1], element[i], d)
        tail = element[-1]
        visited.add(tail)

        


print(len(visited))