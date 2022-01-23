cost = [6,5,7,9,2,2]

cost.sort(reverse=True)

print(cost , sum(cost))

if len(cost)==1:
    print(cost[0])
elif len(cost)==2:
    print(sum(cost))
weHave = 0
for i in range(2, len(cost) ,3):
    weHave+=cost[i]
    print(weHave , cost[i] )
print(sum(cost)-weHave  , weHave)

