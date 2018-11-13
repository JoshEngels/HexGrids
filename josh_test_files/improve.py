# import hex_grid_graph
import mak_test_files.test_n_3 as test3
import random
import copy
import time



def simplify_area(node_list):

    for value_to_decrement in range(7, 1, -1):
        for node in node_list:
            if node.get_value() == value_to_decrement:
                node.try_decrement()


def random_greedy(node_list):

    node_list = list(node_list)
    random.shuffle(list(node_list))
    did_increment = True

    while did_increment:
        did_increment = False
        for node in node_list:
            if node.try_increment():
                did_increment = True


# node_map = hex_grid_graph.hex_grid(7)
# node_map.print_submission()

n = 8
trials = 100
improvements = 1000


first = True
best_score = 0
#
while True:

    t1 = time.time()
    # gets a decent grid for improve to mess around with
    original = test3.fill_ones(n, trials)
    best_score = max(original.calculate_score(), best_score)
    t2 = time.time()
    # print("new original: " + str(t2 - t1))

    if first:
        print(original.calculate_score())
        original.print_submission()
        print()
    first = False

    for i in range(improvements):

        numRows = random.randint(0, 2 * n - 1)
        offset = 0
        if numRows < 2 * n - 2:
            offset = random.randint(0, 2 * n - 2 - numRows)

        node_map = copy.copy(original)
        node_grid = node_map.get_node_grid()

        nodes_to_fuck_up = []
        for j in range(numRows):
            nodes_to_fuck_up.extend(node_grid[j + offset])
        nodes_to_fuck_up = [node for node in nodes_to_fuck_up if node is not None]

        simplify_area(nodes_to_fuck_up)
        random_greedy(nodes_to_fuck_up)

        if node_map.calculate_score() > best_score:
            best_score = node_map.calculate_score()
            print("IMPROVED: " + str(numRows + 1) + " " + str(offset))
            print(node_map.calculate_score())
            node_map.print_submission()
            print()
            original = node_map

    # print("improvements done: " + str(time.time() - t2))
#
# node_map.print_submission()
