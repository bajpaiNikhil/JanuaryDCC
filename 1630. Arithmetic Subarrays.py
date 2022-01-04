nums = [-3, -6, -8, -4, -2, -8, -6, 0, 0, 0, 0]
l = [5, 4, 3, 2, 4, 7, 6, 1, 7]
r = [6, 5, 6, 3, 7, 10, 7, 4, 10]


def checkAs(d):
    hashMap = {}
    smallest = d[0]
    second_smallest = d[1]

    if len(set(d)) == 1:
        return True
    for i in range(len(d)):
        if d[i] not in hashMap:
            hashMap[d[i]] = 1
        else:
            return False
    diff = second_smallest - smallest

    for i in range(len(d) - 1):
        if second_smallest not in hashMap:
            return False
        second_smallest += diff
    return True


for i in range(len(l)):
    d = nums[l[i]:r[i]] + [nums[r[i]]]
    d.sort()
    print(d)
    print(checkAs(d))
