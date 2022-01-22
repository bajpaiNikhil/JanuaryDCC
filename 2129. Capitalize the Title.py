
title = "First leTTeR of EACH Word"
s= ""

for i in title.split():
    print(i)
    if len(i)> 3 :

        s += i[0].upper()
        s += i[1:len(i)].lower()
        s += " "
    else:
        s+=i.lower()
        s+=" "
print(title)

print(s[:-1])