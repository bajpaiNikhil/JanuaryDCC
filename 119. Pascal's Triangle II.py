rowIndex = 5

resRow = [[1] , [1,1]]

if rowIndex == 0:
    print(resRow[0])
elif rowIndex == 1:
    print(resRow[-1])

else:
    tempRow = []
    for i in range(2 ,rowIndex):
        for j in range(i - 1):
            tempRow.append(sum(resRow[-1][j: j+2]))
        resRow.append([1]+tempRow + [1])
        tempRow = []
print(resRow[4])
