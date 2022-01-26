nums = [1,2,3,4]
p = 1
output =  []
for i in nums:
    output.append(p)
    p=p*i
p = 1
print(output)
for i in range(len(nums)-1,-1,-1):
    print(i)
    output[i] = output[i]*p
    p = p*nums[i]
print(output)