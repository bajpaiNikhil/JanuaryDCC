matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
# matrix = [[-1,3]]
# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
#           [10,13,14,17,24],[18,21,23,26,30]]
target = 5

def binarySearch(arrayIs , target , left  , right):
    while right>=left:
        mid =  left+(right-left)//2
        if arrayIs[mid]>target:
            right-=1
        elif arrayIs[mid]<target:
            left+=1
        else:
            return True
    return False



for i in matrix :
    d = binarySearch(i ,  target , left = 0 , right = len(matrix[0])-1)
    print(d)