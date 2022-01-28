s = "aab"


seen = {}

left = 0
right = 0
output = 0

for i in range(len(s)):
    if s[i] not in seen:
        output = max(output , i-left + 1)
        print("from here " , seen , output)
    else:
        if seen[s[i]] < left:
            output = max(output , i-left+1)
            print("from here 1 ", seen, output , seen[s[i]])
        else:
            left = seen[s[i]] + 1
    seen[s[i]] = i
    print("from here 2 ", seen, output)

