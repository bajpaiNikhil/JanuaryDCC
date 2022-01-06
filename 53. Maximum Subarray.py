nums = [-1]

currentMax = 0
globalMax = float("-inf")

for i in range(len(nums)):
    currentMax = max(nums[i] ,  currentMax+nums[i])
    globalMax = max(currentMax , globalMax)
print(globalMax)