image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1

def answer(image , sr ,sc,newColor):
    row = len(image)
    col = len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return (image)
    dfs(image , sr,sc , color , newColor)
    return image

def dfs(image , r ,c , color, newColor):
    if image[r][c] == color:
        image[r][c] = newColor
        if r >= 1:
            dfs(image ,r-1,c, color, newColor)
        if r+1<len(image):
            dfs(image ,r+1,c, color, newColor)
        if c>=1:
            dfs(image ,r,c-1, color, newColor)
        if c+1<len(image[0]):
            dfs(image ,r,c+1, color, newColor)

print(answer(image, sr,sc, newColor=2))