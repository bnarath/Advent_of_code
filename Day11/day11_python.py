import numpy as np

with open('input.txt', 'r') as f:
    grid = np.array([[col for col in row.strip()] for row in f.readlines()])
    
def traverse(h, v, i, j, prev_grid):
    ##################
    #h=1 => right
    #h=-1 => left
    #v=-1 => up (human eyes)
    #v=1 => down
    # h,v tuple for all 8 directions
    # left - (-1,0)
    # right - (1, 0)
    # up - (0, -1)
    # down - (0, 1)
    # diag left up - (-1, -1)
    # diag left down - (-1, 1)
    # diag right up - (1, -1)
    # diag right down - (1, 1)
    ##################
    height, width = prev_grid.shape
    
    while True:
        if ((j+h)>=width and (h==1)) or ((j+h)<0 and (h==-1)) or ((i+v)>=height and (v==1)) or ((i+v)<0 and (v==-1)):
            return 0
        elif prev_grid[i+v,j+h]=='#':
            return 1
        elif prev_grid[i+v,j+h]=='L':
            return 0
        else:
            i+=v
            j+=h

def fill(prev_grid, part=1):
    directions = [(-1,0), (1,0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    new_grid = prev_grid.copy()
    height, width = new_grid.shape
    for i in range(height):
        for j in range(width):
            if (part==1) and (prev_grid[i,j]=='L') and not (np.count_nonzero(prev_grid[max(i-1, 0): min(i+2, height), max(j-1, 0): min(j+2, width)]=='#')):
                new_grid[i,j]='#'
            if (part==2) and (prev_grid[i,j]=='L'):
                occupied_visible_seats = 0
                for direction in directions:
                    occupied_visible_seats+=traverse(*direction, i, j, prev_grid)
                if not occupied_visible_seats:
                    new_grid[i,j]='#'       
    return new_grid

def empty(prev_grid, part=1):
    directions = [(-1,0), (1,0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    new_grid = prev_grid.copy()
    height, width = new_grid.shape
    for i in range(height):
        for j in range(width):
            if (part==1) and (prev_grid[i,j]=='#') and (np.count_nonzero(prev_grid[max(i-1, 0): min(i+2, height), max(j-1, 0): min(j+2, width)]=='#') >= 5):
                new_grid[i,j]='L'
            if (part==2) and (prev_grid[i,j]=='#'):
                occupied_visible_seats = 0
                for direction in directions:
                    occupied_visible_seats+=traverse(*direction, i, j, prev_grid)
                if occupied_visible_seats>=5:
                    new_grid[i,j]='L'
    return new_grid


def calculate_final_occupied_seats(grid, part=1):
    prev_grid = grid.copy()
    rounds = 0
    while True:
        new_grid = fill(prev_grid, part=part)
        rounds+=1
        if np.array_equal(prev_grid, new_grid):
            return np.count_nonzero(new_grid=='#')
        else:
            prev_grid = new_grid.copy()
            new_grid = empty(prev_grid, part=part)
            rounds+=1
            if np.array_equal(prev_grid, new_grid):
                return np.count_nonzero(new_grid=='#')
            else:
                prev_grid = new_grid.copy()
    
    
#part1 - 2368
calculate_final_occupied_seats(grid, part=1)

    
#part2 - 2124
calculate_final_occupied_seats(grid, part=2)