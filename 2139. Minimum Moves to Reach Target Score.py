target = 10
maxDoubles = 4
step = 0

if maxDoubles == 0:
    print(target-1)

else:
    while ( target!=1 and maxDoubles!=0):
        if target%2!= 0:
            step+= 1
            target-=1
        else:
            target >>=1
            maxDoubles-=1
            step+=1
    if maxDoubles == 0 and target!=1:
        print(step+(target-1))
    else:
        print(step ,  target , maxDoubles)

