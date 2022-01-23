from collections import  Counter
nums = [1,3,5,3]
d  = dict(Counter(nums))
res = []
count = 0
for i in d:
    if d[i] == 1:
        if i+1 in d or i-1 in d:
            continue
        else:
            count+=1
            res.append(i)
print(count , res)