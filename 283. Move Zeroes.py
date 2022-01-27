
nums = [0 ,1 ,0 ,3 ,12]

left = 0
#right = len(nums)-1
zeroLimit = 0

for i in range(len(nums)):
    print(nums[i])
    if nums[i] != 0:
        nums[zeroLimit] , nums[i] = nums[i] , nums[zeroLimit]
        #nums[i], nums[zeroLimit] = nums[zeroLimit], nums[i]
        # print(nums[i], nums[zeroLimit] , nums[zeroLimit] ,nums[left] ,i , zeroLimit)
        # i+=1
        zeroLimit+=1
print(nums)

# while(left<=right):
#
#     if nums[left]==0:
#         nums[left],nums[right] = nums[right],nums[left]
#         left+=1
#         right-=1
#     else:
#         left+=1
# print(nums)