from collections import Counter

nums = [4,1,2,1,2]

result = 0

for i in nums:
    result = result ^i
print(result)

