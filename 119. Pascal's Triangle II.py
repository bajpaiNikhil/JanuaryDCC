rowIndex = 3

triangle = [[1] , [1,1]]


if rowIndex == 0:
    print(triangle[0])
elif rowIndex == 2:
    print(triangle[1])

else:
    res = []
    for i in range(2 , rowIndex+1):
        for j in range(i-1):
            res.append(sum(triangle[-1][j:j+2]))
        triangle.append([1] +res+[1])
        res = []
    print(len(triangle))
    print(triangle[-1] , )
