grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]


def exploreSize(grid, r, c, visited):
    rowInbound = 0 <= r < len(grid)
    colInbound = 0 <= c < len(grid[0])

    if not rowInbound or not colInbound:
        return 0
    position = str(r) + "," + str(c)
    if position in visited:
        return 0
    visited.add(position)
    if grid[r][c] == 0:
        return 0
    size = 1
    size += exploreSize(grid, r - 1, c, visited)
    size += exploreSize(grid, r + 1, c, visited)
    size += exploreSize(grid, r, c - 1, visited)
    size += exploreSize(grid, r, c + 1, visited)

    return size


visited = set()

maxSize = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        maxSize = max(exploreSize(grid, i, j, visited), maxSize)
print(maxSize)
