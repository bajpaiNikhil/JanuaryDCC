


intervals = [[1,2],[2,3],[3,4],[1,3]]
result = []
count = 0
for i in intervals:
    if result and result[-1][-1] >=i[0]:
        count+=1
        result[-1][-1] = max(i[1] , result[-1][-1])
    else:
        result.append(i)
print(result)