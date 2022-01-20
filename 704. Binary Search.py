nums = [-1, 0, 3, 5, 9, 12]
target = 9494


def binarySearch(nums, target, left, right):
    if right >= left:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return binarySearch(nums, target, left, mid - 1)
        elif nums[mid] < target:
            return binarySearch(nums, target, mid + 1, right)
    else:
        return False


def search(nums, target):
    return binarySearch(nums, target, left=0, right=len(nums) - 1)


print(search(nums, target))
