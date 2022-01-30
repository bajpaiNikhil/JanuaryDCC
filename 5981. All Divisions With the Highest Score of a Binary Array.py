


from collections import  Counter
nums = [0,0,1,0]
countLeft = 0
countRight = 0
res = []
currentMax= 0
for i in range(len(nums)):
    l = dict(Counter(nums[:i]))
    r = dict(Counter(nums[i:]))
    # if len(l) >0 and 0 in l.keys() and len(r) > 0 and 1 in r.keys():
    #     print(l[0] , r[1])
    # if len(r) > 0 and 1 in r.keys():
    #     print(r[1])
    if len(l) ==0 and len(r)!= 0:
        print()
    if 0 in l.keys():
        countLeft = l[0]
    if 1 in r.keys():
        countRight = r[1]
    if 0 in l.keys() and 1 in r.keys():
        print(l[0] , r[1] , l ,r)
    # countLeft = nums[i:].count(0)
    # countRight = nums[i:].count(1)
    res.append(countLeft+countRight)
print(res)
maxRes = max(res)
print([i for i , x in enumerate(res) if x == maxRes])















