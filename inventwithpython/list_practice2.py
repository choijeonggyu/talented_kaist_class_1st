grid = [['.','.','.','.','.','.'],
['.','0','0','.','.','.'],
['0','0','0','0','.','.'],
['0','0','0','0','0','.'],
['.','0','0','0','0','0'],
['0','0','0','0','0','.'],
['0','0','0','0','.','.'],
['.','0','0','.','.','.'],
['.','.','.','.','.','.']]


for j in range (0, len(grid[0])):
    for i in range (0,len(grid)):
        if i < len(grid) -1:
            print(grid[i][j], end = '')
        else:
            print(grid[i][j])


