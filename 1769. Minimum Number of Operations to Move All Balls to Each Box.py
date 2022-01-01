boxes = "001011"

resultArray = [0] * len(boxes)
ahead = 0
behind = 0

for i in range(len(boxes)):
    if boxes[i] == '1':
        ahead += 1
        resultArray[0] += i

if boxes[0] == '1':
    ahead -= 1
    behind += 1

for i in range(1, len(boxes)):
    resultArray[i] += resultArray[i - 1] - ahead + behind

    if boxes[i] == '1':
        ahead -= 1
        behind += 1
print(resultArray)
