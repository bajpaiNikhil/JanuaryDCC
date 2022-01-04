from collections import defaultdict

n = 4
trust = [[1, 3], [1, 4], [2, 3]]
d = defaultdict(list)
print(d)

for i in trust:
    d[i[0]].append(i[1])
print(d)
print(set.intersection(*map(set, d.values())))

result = set.intersection(*map(set, d.values()))

if (len(result) != 0):
    print("hehehaha", list(result)[0])
else:
    print(-1)

# wrong
