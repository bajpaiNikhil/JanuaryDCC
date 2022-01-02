
from collections import  defaultdict

mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]

d = defaultdict(list)
print(d)
row = len(mat)
colm = len(mat[0])

for i in range(row):
    for j in range(colm):
        d[i-j].append(mat[i][j])
print(d)

for i in d.values():
    i.sort(reverse=True)
print(d)


for i in range(row):
    for j in range(colm):
        mat[i][j] = d[i-j].pop()
print(mat)