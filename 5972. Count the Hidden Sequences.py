differences = [-40]
lower = -46
upper = 53
d = range(lower , upper)
val  = len(list(d))+1
if len(differences)<= val:
    print(0)
else:
    print(val - (len(differences)+1))
