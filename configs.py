from schelling import schelling

class vanilla(schelling):

    def __init__(self):
        super(vanilla, self).__init__(size=(50,50), neighbor_size=1, neighbor_tol=0.5,prob_dist=[0.35, 0.3, 0.35])
        
        self.show_every = 5

class low_tolerance(schelling):

    def __init__(self):
        super(low_tolerance, self).__init__(size=(50,50), neighbor_size=1, neighbor_tol=0.3,prob_dist=[0.35, 0.3, 0.35])

        self.show_every = 5

class high_tolerance(schelling):

    def __init__(self):
        super(high_tolerance, self).__init__(size=(50,50), neighbor_size=1, neighbor_tol=0.7,prob_dist=[0.35, 0.3, 0.35])

        self.show_every = 5
