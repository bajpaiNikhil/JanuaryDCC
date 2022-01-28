from collections import Counter

s1 = "ab"
s2 = "eidbaooo"

ds1 = dict(Counter(s1))
k = len(s1)
print(ds1)

for i in range(len(s2)):
    sub=s2[i:i+k]
    ds2 = dict(Counter(sub))
    if ds1 == ds2:
        print(True)
        break
else:
    print(False)