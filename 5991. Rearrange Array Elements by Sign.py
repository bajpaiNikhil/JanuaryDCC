nums = [3,1,-2,-5,2,-4]

positive = []
negative = []

for i in nums:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)
print(positive , negative)
res = []
for i ,j in zip(positive , negative):
    res+=[i,j]
print(res)