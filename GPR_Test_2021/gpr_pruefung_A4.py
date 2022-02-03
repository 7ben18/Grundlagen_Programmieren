import copy

grid = ['..........', '.###.##...', '.....##...', '.......##.', '.......##.', '..........']

# Game of Life, Nachbarn zaehlen
def living_neighbours(grid,row,col):
    cnt = 0
    if 0 < row and grid[row-1][col] == "#": # Oben
        cnt += 1
    if row < len(grid) and grid[row+1][col] == "#": # unten
        cnt += 1
    if 0 < col and grid[row][col-1] == "#": # Links
        cnt += 1
    if col < len(grid) and grid[row][col+1] == "#": # Rechts
        cnt += 1
    return cnt

print(living_neighbours(grid, 1, 1))
print(living_neighbours(grid, 1, 2))
print(living_neighbours(grid, 3, 1))


# Step grid funktioniert nicht! (Teilpunkte)
def step(grid):
    new_grid = grid.copy()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            neighbours = living_neighbours(grid, row, col)
            if grid[row][col] == "." and neighbours == 2:
                new_grid[row][col] = "#"
            elif grid[row][col] == "#" and neighbours < 2 or neighbours > 3:
                new_grid[row][col] = "."
            else:
                new_grid[row][col] = grid[row][col]
    return new_grid


print(step(grid))