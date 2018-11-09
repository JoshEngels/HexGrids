# Implementatipon of a hex grid class, where hex grids are stored as a graph that represents the nodes. Has inner nodes
# that map to their neighbors.



class hex_node:


    def __init__(neighbors = [], id = 1, ):
        self.neighbors = neighbors
        self.id = id



    def is_corner(self):
        return len(self.neighbors) == 3

    def is_edge(self):
        return len(self.neighbors) == 4

    def is_center(self):
        return len(self.neighbors) == 6

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, new_neighbor):
        self.enighbors.append(new_neighbor)
