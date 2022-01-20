

matrix = [[1,1,1],[1,2,3],[1,2,3]]

row = len(matrix)
colm = len(matrix[0])

for i , j in zip(matrix, zip(*matrix)):
    print(i , j)
    if len(set(i)) != row or len(set(j)) != colm:
        print(False)
        break
    else:
        print(True)