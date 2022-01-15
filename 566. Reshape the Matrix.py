mat = [[1, 2], [3, 4]]
r = 1
c = 4

rowLength = len(mat)
colmLength = len(mat[0])

if rowLength*colmLength != r*c:
    print(mat)

l = []
for i in range(rowLength):
    for j in range(colmLength):
        l.append(mat[i][j])
print(l)

k= 0
new_mat = list()
for i in range(r):
    print(i)
    new_mat.append(l[k:k+c])
    k+=c
print(new_mat)
