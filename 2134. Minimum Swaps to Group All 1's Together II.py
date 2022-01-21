nums = [0,1,1,1,0,0,1,1,0]
n = len(nums)
ones = nums.count(1)
print(ones)
for i in range(n*2):
    print(nums[i%n] , end="")
    print(nums[i%n - ones])
