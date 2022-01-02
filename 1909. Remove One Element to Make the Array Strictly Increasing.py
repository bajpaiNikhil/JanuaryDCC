nums = [1, 2, 1, 3, 4]

count = 0
index = 0
arrayLength = len(nums)

for i in range(arrayLength - 1):
    if nums[i] >= nums[i + 1]:
        index = i
        count += 1

if count == 0:
    print(True)

elif count == 1:

    if index == 0 or index == arrayLength - 2:
        print(True)

    if nums[index - 1] < nums[index + 1] or (index + 2 < arrayLength and nums[index] < nums[index + 2]):
        print(True)

else:
    print(False)