s = "abcdefghij"
k = 3
fill = "x"
a = len(s)
b = a//k
c= a%k
s += ((c*k)-1) * 'x'
m = []

for i in range( 0 , len(s) , k):
    m.append(s[i:i+k])
print(m)
