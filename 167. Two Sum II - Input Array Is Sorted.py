numbers = [5,25,75]
target = 100


def binarySearchTwoSum(nums, targets, left, right):
    while right>=left:
        mid = left+(right-left)//2
        if nums[mid] == targets:
            print(mid, nums[mid], targets)
            return mid+1
        elif nums[mid] >targets:
            return binarySearchTwoSum(nums , targets ,left , mid-1)
        else:
            return binarySearchTwoSum(nums , targets ,mid+1 , right)



def twoSum(numbers , target):
    for i in range(len(numbers)):
        print(i,end=" ")
        d = binarySearchTwoSum(numbers[i:] , target-numbers[i] , left = 0 ,right=len(numbers[i:])-1)
        print(d)
        if d is not None:
            return [i+1 , d]
    return False
print(twoSum(numbers , target))