

nums = [8,19,4,2,15,3]
nums.sort()
original = 2
count = 0
for i in nums:
    if original == i:
        i*=2
        count = i
        original = i
print(count)

