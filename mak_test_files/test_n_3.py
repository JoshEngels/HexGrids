import time
import hex_grid_graph
import random

# from tqdm import tqdm


### Version that iterates through each node randomly
# def random_descent(size = 3, trials = 50, infinite = False):
#     best_score = 0
#     best_grid = None
#
#     while True:
#         for _trail in range(trials):
#             hexes = hex_grid_graph.hex_grid(size)
#             changed = True
#             nodes_list = list(hexes.get_node_list())
#             while changed:
#                 changed = False
#                 random.shuffle(nodes_list)
#                 for node in nodes_list:
#                     if node.try_increment():
#                         changed = changed or True
#             score = hexes.calculate_score()
#             if score > best_score:
#                 best_score = score
#                 best_grid = hexes
#
#         print("Best Score:", best_grid.calculate_score())
#         best_grid.print_submission()
#         if not infinite:
#             break
#
#     return best_grid

# ### Random descent with placeback.
def random_descent(size = 3, trials = 50, infinite = False):
    best_score = 0
    best_grid = None

    while True:
        for _trail in range(trials):
            hexes = hex_grid_graph.hex_grid(size)
            changed = True
            nodes_list = list(hexes.get_node_list())
            count_limit = len(nodes_list) * 3
            while changed:
                changed = False
                counter = 0
                if counter < count_limit:
                    counter += 1
                    node = random.choice(nodes_list)
                    if node.try_increment():
                        counter = 0

                random.shuffle(nodes_list)
                for node in nodes_list:
                    changed = changed or node.try_increment()
            score = hexes.calculate_score()
            if score > best_score:
                best_score = score
                best_grid = hexes

        print("Best Score:", best_grid.calculate_score())
        best_grid.print_submission()
        if not infinite:
            break

    return best_grid

def far_increment(node):
    if not node.try_increment() and node.get_value()>1:
        node.set_value(node.get_value() - 1)
        change = False
        invalid = False
        for neighbor in node.get_neighbors():
            invalid = invalid or not neighbor.is_valid()
        if invalid:
            node.try_increment()
            return False

        for neighbor in node.get_neighbors():
            change = change or neighbor.try_increment()
        return change
    else:
        return True
#
# # ### Random descent with placeback.
def random_improvement(size = 3, itteration = 50, infinite = False):
    best_score = 0
    best_grid = None
    hexes = hex_grid_graph.hex_grid(size)

    while True:
        count = 0
        for _trail in range(itteration):
            nodes_list = list(hexes.get_node_list())
            count_limit = len(nodes_list) * 3
            node = random.choice(nodes_list)
            changed = True
            nodes_list = list(hexes.get_node_list())
            while changed:
                changed = False
                counter = 0
                if counter < count_limit:
                    counter += 1
                    node = random.choice(nodes_list)
                    if node.try_increment():
                        counter = 0

                random.shuffle(nodes_list)
                for node in nodes_list:
                    changed = changed or node.try_increment()

            score = hexes.calculate_score()
            if score > best_score:
                best_score = score
                print("Best Score:", best_score)
                best_grid = hexes.print_submission()

            if _trail == itteration - 1:
                print("Current Score:", hexes.calculate_score())
                hexes.print_submission()

            random.shuffle(nodes_list)
            for node in nodes_list:
                far_increment(node)


        print("Best Score:", best_score)
        print(best_grid)

        if not infinite:
            break

    return best_grid

def fixed(node, offset = 0, check = 1):
    # Returns True, if the node, is one of the fixed nodes of one.
    value = node.get_value()
    coord = node.get_coordinate()
    if value == check:
        return ((coord[0]*2+coord[1]) + offset) % 7 == 0
    return False


# Essentially the same as random_descent, but leaves fixed nodes always at 1.
def fill_ones(size = 3, trials = 50, infinite = False):
    best_score = 0
    best_grid = None


    while True:
        for _trail in range(trials):
            hexes = hex_grid_graph.hex_grid(size)
            offset = random.randint(0, 6)
            nodes_list = list(hexes.get_node_list())

            count_limit = len(nodes_list) * 3
            changed = True
            while changed:
                changed = False
                counter = 0
                if counter < count_limit:
                    counter += 1
                    node = random.choice(nodes_list)
                    if not fixed(node, offset):
                        if node.try_increment():
                            counter = 0

                random.shuffle(nodes_list)
                for node in nodes_list:
                    if not fixed(node, offset):
                        changed = changed or node.try_increment()
            score = hexes.calculate_score()
            if score > best_score:
                best_score = score
                best_grid = hexes

        print("Best Score:", best_grid.calculate_score())
        best_grid.print_submission()
        if not infinite:
            break

    return best_grid


# best_grid = random_improvement(5, 1000, True)
best_grid = fill_ones(6, 1000, True)

# new_grid = hex_grid_graph.hex_grid(5)
#
# display = ""
# for row in new_grid.get_node_grid():
#     for node in row:
#         show = "----- "
#         if node is not None:
#             show = fixed(node)
#             if show:
#                 show = "True  "
#             else:
#                 show = "False "
#
#         display += show + " "
#
#     display += "\n"
# print(display)

