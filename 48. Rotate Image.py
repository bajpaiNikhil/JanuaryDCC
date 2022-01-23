#matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix  =  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix.reverse()
row = len(matrix)
col = len(matrix[0])
# print(matrix)
# matrix[0],matrix[-1] = matrix[-1],matrix[0]
# print(matrix)
# for i in range(row):
#    for j in range(i+1 , col):
#        matrix
# print(matrix)

for i in range(row):
    for j in range(i +1 , col):
        print(matrix[i][j],matrix[j][i],matrix[j][i],matrix[i][j])
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
print(matrix)

# matrix[:] = zip(*matrix[::-1])
# print(matrix)