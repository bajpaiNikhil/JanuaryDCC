from collections import Counter


nums = [2,2,1,1,1,2,2]

d= dict(Counter(nums).most_common())

print(d)
print(list(d.keys())[0])