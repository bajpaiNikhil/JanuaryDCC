

nums = [1,1,1,3,3,4,3,2,4,2]

a  = set()

for i in nums:
    if i in a:
        print(True)
    else:
        a.add(i)
print(a)
