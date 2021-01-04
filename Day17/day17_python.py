import numpy as np

with open('input.txt', 'r') as f:
    file = [list(line.strip()) for line in f.readlines()]

def part1(file):
    grid = np.array(file)
    grid = grid.reshape(*grid.shape, 1)
    rounds=6
    for R in range(1,rounds+1):
        new_grid = np.full(np.array(list(grid.shape))+2, '.')
        x,y,z = new_grid.shape
        x0, y0, z0 = -R,-R,-R
        new_grid[1:-1, 1:-1, 1:-1] = grid
        grid = new_grid.copy()
        for i in range(x0,x0+x):
            for j in range(y0,y0+y):
                for k in range(z0,z0+z):
                    cube = new_grid[i+R, j+R, k+R]
                    neighbours = np.count_nonzero(grid[max(i-1+R,0):min(i+2+R, x),max(j-1+R,0):min(j+2+R, y),max(k-1+R,0):min(k+2+R, z)]=='#')
                    if (cube == '#') and (((neighbours-1) != 2) and ((neighbours-1) != 3)):
                        new_grid[i+R, j+R, k+R] = '.'
                    if (cube == '.') and (neighbours == 3) :
                        new_grid[i+R, j+R, k+R] = '#'
        grid = new_grid
    return np.count_nonzero(grid=='#')


def part2(file):
    grid = np.array(file)
    grid = grid.reshape(*grid.shape, 1, 1)
    rounds=6
    for R in range(1,rounds+1):
        new_grid = np.full(np.array(list(grid.shape))+2, '.')
        x,y,z,w = new_grid.shape
        x0, y0, z0, w0 = -R,-R,-R,-R
        new_grid[1:-1, 1:-1, 1:-1, 1:-1] = grid
        grid = new_grid.copy()
        for i in range(x0,x0+x):
            for j in range(y0,y0+y):
                for k in range(z0,z0+z):
                    for l in range(w0,w0+w):
                        hypercube = new_grid[i+R, j+R, k+R, l+R]
                        neighbours = np.count_nonzero(grid[max(i-1+R,0):min(i+2+R, x),max(j-1+R,0):min(j+2+R, y),max(k-1+R,0):min(k+2+R, z), max(l-1+R,0):min(l+2+R, w)]=='#')
                        if (hypercube == '#') and (((neighbours-1) != 2) and ((neighbours-1) != 3)):
                            new_grid[i+R, j+R, k+R, l+R] = '.'
                        if (hypercube == '.') and (neighbours == 3) :
                            new_grid[i+R, j+R, k+R, l+R] = '#'
        grid = new_grid
    return np.count_nonzero(grid=='#')

print(part1(file))
print(part2(file))