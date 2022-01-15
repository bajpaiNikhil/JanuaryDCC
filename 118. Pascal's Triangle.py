numRows = 5

"""
if numRows = 5
               [
                     [1],
                    [1,1],
                   [1,2,1],
                  [1,3,3,1],
                 [1,4,6,4,1]
               ]
"""
res = [[1] , [1,1]]
if numRows == 1:
    print(res[0])
elif numRows == 2:
    print(res)
else:
    row = []
    for i in range(2,numRows):
        for j in range(i-1) :
            row.append(sum(res[-1][j:j+2]))
        res.append([1]+row+[1])
        row=[]

print(res)
