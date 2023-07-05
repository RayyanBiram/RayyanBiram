def minesweeper(grid):
    # Determine the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])
    
    # Create an empty result grid
    result = [["0" for j in range(cols)] for i in range(rows)]
    
    # Iterate over each spot in the grid
    for i in range(rows):
        for j in range(cols):
            # If the spot is a mine, mark it as such in the result grid
            if grid[i][j] == "#":
                result[i][j] = "#"
            else:
                # Count the number of adjacent mines
                count = 0
                for ii in range(max(0, i-1), min(i+2, rows)):
                    for jj in range(max(0, j-1), min(j+2, cols)):
                        if grid[ii][jj] == "#":
                            count += 1
                
                # Set the count in the result grid
                result[i][j] = str(count)
    
    return result

grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

result = minesweeper(grid)

for row in result:
    print(row)