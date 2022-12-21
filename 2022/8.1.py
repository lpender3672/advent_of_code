
trees = []
with open('2022/8.txt', 'r') as f:
    for l in f:
        l = list(l.strip())
        trees.append([int(i) for i in l])

n = len(trees)
m = len(trees[0])

visible = 2 * n + 2 * m - 4

# find internal visable trees

for i in range(1, n-1):
    row_max = max(trees[i])
    for j in range(1, m-1):
        tree = trees[i][j]
        collumn = [trees[k][j] for k in range(n)]
        if max(trees[i][:j]) < tree or max(trees[i][j+1:]) < tree:
            visible += 1
        elif max(collumn[:i]) < tree or max(collumn[i+1:]) < tree:
            visible += 1

print(visible)
