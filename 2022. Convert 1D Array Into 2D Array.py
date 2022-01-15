original = [1, 2, 3, 4]
m = 2
n = 2

if m * n != len(original):
    print([])
new_mat = []

k = 0
for i in range(m):
    new_mat.append(original[k:k+n])
    k+=n
print(new_mat)