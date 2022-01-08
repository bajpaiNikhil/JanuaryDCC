from collections import defaultdict

nums = [1,2,2,3,1,4,2]

d =  defaultdict(list)

for index , value in enumerate(nums):
    d[value].append(index)

degree = max(len(v) for v in d.values())
k = float('-inf')
for i in d:
    if len(d[i]) == degree:
        k = d[i][-1] - d[i][0] + 1
        k = min(k , k)
print(k)
