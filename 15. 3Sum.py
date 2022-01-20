nums = [-1,0,1,2,-1,-4]


def threeSum(nums):
    if not nums or len(nums) < 3:
        return []
    nums.sort()
    result, N = [], len(nums)

    for i in range(N - 1):
        target = - nums[i]
        # convert 3sum to 2sum problem
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        s, e = i + 1, N - 1
        while s < e:
            if nums[s] + nums[e] == target:
                result.append([nums[i], nums[s], nums[e]])
                s += 1
                e -= 1
                while s < e and nums[s] == nums[s - 1]:
                    s += 1
                while s < e and nums[e] == nums[e + 1]:
                    e -= 1
            elif nums[s] + nums[e] < target:
                s += 1
            elif nums[s] + nums[e] > target:
                e -= 1

    return result

print(threeSum(nums))