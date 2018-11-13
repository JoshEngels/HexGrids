# Implementatipon of a hex grid class, where hex grids are stored as a graph that represents the nodes. Has inner nodes
# that map to their neighbors.



class hex_node:

    def __init__(self, neighbors = [], value = -1, id = 1, coordinate = (0,0)):
        self.neighbors = neighbors
        self.value = value
        self.id = id
        self.coordinate = coordinate

    def __str__(self):
        return str(self.value)

    def is_corner(self):
        return len(self.neighbors) == 3

    def is_edge(self):
        return len(self.neighbors) == 4

    def is_center(self):
        return len(self.neighbors) == 6

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, new_neighbor):
        self.neighbors.append(new_neighbor)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_coordinate(self):
        return self.coordinate

    def get_id(self):
        return self.id

    def is_valid(self):
        neighbor_vals = [neighbor.get_value() for neighbor in self.neighbors]
        for req in range(1, self.value):
            if req not in neighbor_vals:
                return False
        return True

    def try_increment(self):
        """
        Will have problems with parallel implementations
        :return:
        """
        return self.try_change(1)

    def try_decrement(self):
        return self.try_change(-1)

    def try_change(self, change):
        self.value += change
        if not self.is_valid():
            self.value -= change
            return False
        can_neighbors = [neighbor.is_valid() for neighbor in self.neighbors]
        if False in can_neighbors:
            self.value -= change
            return False
        return True




class hex_grid:

    def __init__(self, size):
        self.size = size
        self.nodes_grid = []
        unique_id = 1
        for row in range(size):
            new_nodes = []
            for col in range(row + size):
                new_node = hex_node([], 1, unique_id, (row, col))
                unique_id += 1
                new_nodes.append(new_node)
            new_nodes.extend([None for _dummy in range((size - row) - 1)])
            self.nodes_grid.append(new_nodes)
        for row in range(size, (2 * size) - 1):
            new_nodes = [None for _dummy in range((row - size) + 1)]
            for col in range(3 * size - (row + 2)):
                new_node = hex_node([], 1, unique_id, (row, col + (row - size + 1)))
                unique_id += 1
                new_nodes.append(new_node)
            self.nodes_grid.append(new_nodes)

        for row in self.nodes_grid:
            for node in row:
                if node is not None:
                    coords = node.get_coordinate()
                    neighbors = []
                    for direction in [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]:
                        try:
                            if coords[0] + direction[0] >= 0 and coords[1] + direction[1] >= 0:
                                neighbor = self.nodes_grid[coords[0] + direction[0]][coords[1] + direction[1]]
                                if neighbor is not None:
                                    node.add_neighbor(neighbor)
                        except:
                            None

        self.nodes_list = []
        for row in self.nodes_grid:
            for node in row:
                if node is not None:
                    self.nodes_list.append(node)

    def __copy__(self):
        copied_grid = hex_grid(self.size)  # at first the same size
        for original_node, copy_node in zip(self.get_node_list(), copied_grid.get_node_list()):
            original_node.set_value(copy_node.get_value())  # ids should be the same, so no need to set
        return copied_grid

    def __eq__(self, other):
        for original_node, copy_node in zip(self.get_node_list(), other.get_node_list()):
            if original_node.get_value() != copy_node.get_value():  # if all values the same, they  are the same
                return False
        return True

    def get_node_grid(self):
        return self.nodes_grid

    def get_node_list(self):
        return self.nodes_list

    def get_size(self):
        return self.size

    def print_coords(self):
        string = ""
        for row in self.nodes_grid:
            for val in row:
                if val == None:
                   string += "(None) "
                else:
                    string += str(val.get_coordinate()) + " "
            string += "\n"
        print(string)

    def print_vals(self):
        string = ""
        for row in self.nodes_grid:
            for val in row:
                if val == None:
                   string += "- "
                else:
                    string += str(val.get_value()) + " "
            string += "\n"
        print(string)

    def print_ids(self):
        string = ""
        for row in self.nodes_grid:
            for val in row:
                if val == None:
                   string += "- "
                else:
                    string += str(val.get_id()) + " "
            string += "\n"
        print(string)

    def is_valid(self):
        for row in self.nodes_grid:
            for val in row:
                if val is not None:
                   if not val.is_valid():
                       return False
        return True

    def calculate_score(self):
        score = 0
        for row in self.nodes_grid:
            for val in row:
                if val is not None:
                   score += val.get_value()
        score -= ((3 * (self.size ** 2)) - (3 * self.size) + 1)
        return score

    def print_submission(self):
        string = ""
        no_new_line = True
        for row in self.nodes_grid:
            if not no_new_line:
                string += "),\n"
            else:
                no_new_line = False
            string += "("
            no_comma = True
            for val in row:
                if val is not None:
                    if not no_comma:
                        string += ", "
                    else:
                        no_comma = False
                    string += str(val.get_value())
        string += ")"
        print(string)
        return string



# grid_5 = hex_grid(5)
#
# grid_5.print_ids()
# grid_5.print_vals()
# print(grid_5.calculate_score())
# grid_5.print_coords()
#
# changed = True
# while changed:
#     changed = False
#     for node in grid_5.get_node_list():
#         changed = changed or node.try_increment()
# grid_5.print_vals()
# print(grid_5.calculate_score())
# grid_5.print_submission()