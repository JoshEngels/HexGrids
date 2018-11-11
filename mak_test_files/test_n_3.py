import time
import hex_grid_graph
import random

# from tqdm import tqdm


def random_descent(size = 3, trials = 50):
    best_score = 0
    best_grid = None

    for _trail in range(trials):
        hexes = hex_grid_graph.hex_grid(size)
        changed = True
        nodes_list = list(hexes.get_node_list())
        while changed:
            changed = False
            random.shuffle(nodes_list)
            for node in nodes_list:
                changed = changed or node.try_increment()
        score = hexes.calculate_score()
        if score > best_score:
            best_score = score
            best_grid = hexes

    return best_grid

best_grid = random_descent(4, 1000)
print("Score:", best_grid.calculate_score())
best_grid.print_submission()
