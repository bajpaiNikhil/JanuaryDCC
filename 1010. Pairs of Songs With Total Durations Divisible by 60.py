time = [30, 20, 150, 100, 40]
count = 0
n = len(time)
for i in range(len(time)):
    for j in range(len(time)):
        if i < j and ((time[i] + time[j]) % 60 == 0):
            print(time[i], time[j])
            count += 1
print(count)
