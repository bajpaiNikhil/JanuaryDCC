nums = [1, 3, 5, 6]
target = 2


def insertValue(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
            print(right , "right" , nums[mid] , mid)
        else:
            left = mid + 1
            print(left , "left" ,  nums[mid] , mid)
    return left


print(insertValue(nums, target))
