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
    nbhd = [grid[k] for k in list(neighbors(xy, m, n, neighbor_size))]
    cnt = nbhd.count(grid[xy]) / len(nbhd)
    
    if cnt < tolerance:
        return True
    else:
        return False

class schelling:

    """
    Class for Schelling Segregation 2-Agent Model

        - Initialization 
            size : size of the grid
            neighbor_size : radius definition of the neighborhood
            neighbor_tol : tolerance for the neighborhood
            prob_dist : probability distribution for the initialization of the grid
            max_frame : maximum iteration to render (default : 50)
            show_every : steps of iterations to rander (default : 5)
    """

    def __init__(self, size, neighbor_size, neighbor_tol, prob_dist, max_frame=50, show_every=5):
        self.size = size
        self.neighbor_size = neighbor_size
        self.neighbor_tol = neighbor_tol
        self.prob_dist = prob_dist
        
        self.max_frame = max_frame
        self.show_every = show_every

    def run(self):
        # Take height (# rows) and width (# cols)
        h, w = self.size

        # Initialize grid
        grid = np.random.choice(3, size=self.size, p=self.prob_dist) - 1

        # Run for each frame
        frame = 0
        while frame < self.max_frame:

            if not frame % self.show_every:
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
                        if similarity(grid, (i,j), self.neighbor_size, self.neighbor_tol):
                            empty1, empty2 = random.choice(np.argwhere(grid == 0))
                            grid[empty1, empty2], grid[(i,j)] = grid[(i,j)], 0
                        else:
                            pass

            frame = frame + 1
                
if __name__ == '__main__':
    
    import configs

    vn = configs.vanilla().run()
    lt = configs.low_tolerance().run()
    ht = configs.high_tolerance().run()
