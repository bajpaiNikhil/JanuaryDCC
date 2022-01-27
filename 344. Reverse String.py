

s = ["h","e","l","l","o"]

print(s[::-1])
left=0
right=len(s)-1

for i in range(len(s)//2):
    s[i],s[right] = s[right],s[i]
    right-=1
print(s)