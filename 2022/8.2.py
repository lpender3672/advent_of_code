
trees = []
with open('2022/8.txt', 'r') as f:
    for l in f:
        l = list(l.strip())
        trees.append([int(i) for i in l])

n = len(trees)
m = len(trees[0])
best_score = 1

for i in range(1,n-1):
    for j in range(1,m-1):
        score = 1
        tree = trees[i][j]
        collumn = [trees[k][j] for k in range(n)]

        k = j - 1
        while k > 0 and trees[i][k] < tree:
            k -= 1
        score *= (j - k)
        k = j + 1
        while k < n - 1 and trees[i][k] < tree:
            k += 1
        score *= (k - j)
        k = i - 1
        while k > 0 and trees[k][j] < tree:
            k -= 1
        score *= (i - k)
        k = i + 1
        while k < m - 1 and trees[k][j] < tree:
            k += 1
        score *= (k - i)
        if score > best_score:
            best_score = score
        
print(best_score)
