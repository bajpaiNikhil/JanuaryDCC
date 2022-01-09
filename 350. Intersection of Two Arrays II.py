from collections import Counter

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums2.sort()
nums1.sort()
i = 0
j = 0
result = []
#
# while i < len(nums1) and j < len(nums2):
#     if nums1[i] == nums2[j]:
#         result.append(nums1[i])
#         i += 1
#         j += 1
#     elif nums1[i] > nums2[j]:
#         j += 1
#     else:
#         i += 1
# print(result)


d = Counter(nums1)
e = Counter(nums2)

print(d, e)

for i in d:
    if i in e:
        result.extend([i] * min(d[i], e[i]))
print(result)
