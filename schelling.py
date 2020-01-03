import random
import copy

from itertools import product

import numpy as np
import matplotlib.pyplot as plt

def neighbors(xy, num_rows, num_cols, neighbor_size):
    for c in product(*(range(n-neighbor_size, n+neighbor_size+1) for n in xy)):
        if (c != xy) and (c[0] in range(num_rows)) and (c[1] in range(num_cols)):
            yield c

def similarity(grid, xy, neighbor_size, tolerance):
    # Need to move (True) if fraction of friendlies are below tolerance
    m, n = grid.shape
    nbhd = [grid[n] for n in list(neighbors(xy, m, n, neighbor_size))]
    cnt = nbhd.count(grid[xy]) / len(nbhd)
    
    if cnt < tolerance:
        return True
    else:
        return False

def schelling_model(size, neighbor_size, tolerance, prob_dist, max_frame=1e5, show_every=10):
    # Take height (# rows) and width (# cols)
    h, w = size

    # Initialize grid
    grid = np.random.choice(3, size=size, p=prob_dist) - 1

    # Run for each frame
    frame = 0
    while frame < max_frame:


        if not frame % show_every:
            fig, ax = plt.subplots()
            fig.suptitle('Iteration %d' % frame, fontsize=10)
            ax.matshow(grid)

            # Press 'q' to proceed to the next snapshot
            plt.show()
            
        
        for i in range(h):
            for j in range(w):
                
                if grid[(i,j)] == 0:
                    pass
                else:
                    if similarity(grid, (i,j), neighbor_size, tolerance):
                        empty1, empty2 = random.choice(np.argwhere(grid == 0))
                        grid[empty1, empty2], grid[(i,j)] = grid[(i,j)], 0
                    else:
                        pass

        frame = frame + 1
                
if __name__ == '__main__':
    grid_size = (50, 50)
    neighbor_size = 1
    neighbor_tol = 0.5
    init_prob_dist = [0.35, 0.3, 0.35]


    schelling_model(grid_size, neighbor_size, neighbor_tol, init_prob_dist, show_every=5)