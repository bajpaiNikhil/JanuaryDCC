from collections import Counter

s = "tree"
d = dict(Counter(s))
newS = ""
sortDict = sorted(d.items(), key=lambda x: x[1], reverse=True)
for i in sortDict:
    newS+=i[0]*i[1]
print(newS)