nums = [-71,-71,93,-71,40]
# nums = [-3,3,3,90]
# nums = [11,7,2,15]
nums.sort()
a = min(nums)
b = max(nums)
res = []
count = 0
for i in nums:
    if i != a and i!=b :
        count+=1
        res.append(i)
    else:
        continue
print(res ,count)


# c = nums.count(a)
# d = nums.count(b)
#
# print(nums.count(a))
# print(nums.count(b))
#
# print(nums , nums.index(a) ,nums[::-1].index(a) ,  a)
# lastMin = nums[::-1].index(a)
# firstMax = nums.index(b)
#
# # print(len(nums[lastMin:firstMax])-1)
# if c >= 2 or :
#     print(len(nums[lastMin:firstMax]) - 1)
# else:
#     print(len(nums[1:-1]))