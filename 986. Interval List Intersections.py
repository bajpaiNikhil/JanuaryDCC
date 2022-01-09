firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

i = 0
j = 0
answer = []

while i < len(firstList) and j < len(secondList):
    current = [max(firstList[i][0], secondList[j][0]) , min(firstList[i][1] , secondList[j][1])]
    print(current)
    if current[0] <= current[1]:
        answer.append(current)
    if firstList[i][1] <= secondList[j][1]:
        i += 1
    else:
        j += 1
print(answer)
