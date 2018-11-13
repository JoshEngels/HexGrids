# import hex_grid_graph
import mak_test_files.test_n_3 as test3
import random

# ToDo: Write a general random greedy that takes in a list of nodes and greedies it. Doesn't have to be the whole graph


def simplify_area(node_list):

    for value_to_decrement in range(7, 1, -1):
        for node in node_list:
            if node.get_value() == value_to_decrement:
                node.try_decrement()

def random_greedy(node_list):

    node_list = random.shuffle(list(node_list))
    did_increment = True

    while did_increment:
        did_increment = False
        for node in node_list:
            if node.try_increment():
                did_increment = True


# node_map = hex_grid_graph.hex_grid(7)
# node_map.print_submission()
node_map = test3.get_good_grid()
print()
node_grid = node_map.get_node_grid()
nodes_to_fuck_up = []
nodes_to_fuck_up.extend(node_grid[0])
nodes_to_fuck_up.extend(node_grid[1])
nodes_to_fuck_up.extend(node_grid[2])
nodes_to_fuck_up.extend(node_grid[3])
nodes_to_fuck_up.extend(node_grid[4])

nodes_to_fuck_up = [node for node in nodes_to_fuck_up if node != None]

#
simplify_area(nodes_to_fuck_up)
#
node_map.print_submission()
