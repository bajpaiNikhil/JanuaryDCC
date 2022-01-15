from collections import  Counter

nums = [1,1,1,2,2,3]
k = 2
d = Counter(nums).most_common()
print([i[0] for i in d[:k]])



