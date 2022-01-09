nums = [-7,-3,2,3,11]

leftPtr = 0
rightPtr = len(nums)-1
resultArray = []
while leftPtr <= rightPtr:

    if abs(nums[leftPtr]) > abs(nums[rightPtr]) :
        resultArray.append(nums[leftPtr] * nums[leftPtr])
        leftPtr+=1
    else:
        resultArray.append(nums[rightPtr] * nums[rightPtr])
        rightPtr-=1

print(resultArray[::-1])
