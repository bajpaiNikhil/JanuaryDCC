s = "God Ding"


def reverseString(i):
    i = list(i)
    right = len(i) - 1
    for j in range(len(i)//2):
        i[right], i[j] = i[j], i[right]
        right -= 1
    return "".join(i)


d = ""
for i in s.split():
    d+= (reverseString(i)+" ")
print(d)
