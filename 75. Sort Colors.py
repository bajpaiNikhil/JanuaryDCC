nums = [2, 0, 2, 1, 1, 0]

zeroBoundary  = 0 #tracks last 0
currentIndex  = 0 #tracks last 1
TwoBoundary = len(nums)-1 #tracks first 2

while currentIndex<= TwoBoundary:
    if nums[currentIndex] == 0:
        nums[currentIndex] , nums[zeroBoundary] =  nums[currentIndex] ,  nums[zeroBoundary]
        currentIndex+=1
        zeroBoundary +=1
    elif nums[currentIndex] == 2:
        nums[currentIndex] ,  nums[TwoBoundary] = nums[TwoBoundary] ,nums[currentIndex]
        TwoBoundary-=1
    else:
        currentIndex+=1

print(nums)



