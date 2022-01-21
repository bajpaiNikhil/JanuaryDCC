intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

d = sorted(intervals, key=lambda i: i[0])
print(d)
extraArray = []
for i in d:
    print(i)
    if extraArray and i[0] <= extraArray[-1][1]:
        extraArray[-1][1] = max(extraArray[-1][1], i[-1])
    else:
        extraArray += [i]
print(extraArray)
