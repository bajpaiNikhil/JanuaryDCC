

intervals =  [[1,100],[11,22],[1,11],[2,12]]
d = sorted(intervals, key=lambda i: i[1])
print(d)
result = []
count = 0
for i in d:
    print(i)
    if result and i[0]<result[-1][1]:
        count+=1

    else:
        result.append(i)
print(result ,count)
