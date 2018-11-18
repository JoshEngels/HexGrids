import hex_grid_graph
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


def update(graph, nodes):
    old = copy.copy(graph)

    simplify_area(nodes)
    random_greedy(nodes)

    if old.calculate_score() >= graph.calculate_score():
        graph = old

    return graph


def hex_improve(graph, runs_through_the_graph, max_hex_size, best_score_so_far):
    """
    Loops through every element in the graph multiple times and tries to improve hexes from size 1 to max_hex_size
    at every one of those elements
    :param graph: The graph to attempt to improve
    :param runs_through_the_graph: The number of times to loop through every element in the graph
    :param max_hex_size: The max hex size to test
    :param best_score_so_far: The best score attained for this n so far. The function will print
    out scores found greater than this score, as well as grids.
    :return: The graph, improved if possible or otherwise the same
    """
    best_score_so_far = max(best_score_so_far, graph.calculate_score())

    for temp in range(runs_through_the_graph):

        for i in range(len(graph.get_node_list())):
            for j in range(1, max_hex_size + 1):

                node_list = graph.get_node_list()
                graph = update(graph, hex_grid_graph.hex_grid.get_hex(node_list[i], j))

                if graph.calculate_score() > best_score_so_far:
                    best_score_so_far = original.calculate_score()
                    print(best_score_so_far)
                    original.print_submission()
                    print()

    return graph


original = hex_grid_graph.hex_grid.create_from_2d_list([
(4, 3, 5, 4, 3, 5, 4, 3, 4, 2),
(2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 3),
(3, 4, 7, 6, 4, 3, 4, 3, 4, 5, 6, 4),
(1, 6, 5, 3, 5, 7, 6, 5, 6, 7, 3, 2, 1),
(1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 7, 6, 4),
(4, 5, 6, 7, 5, 4, 3, 4, 3, 4, 6, 4, 5, 3, 2),
(3, 2, 3, 4, 3, 7, 6, 5, 7, 6, 5, 3, 2, 1, 4, 1),
(5, 1, 5, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4, 6, 7, 5, 3),
(4, 2, 7, 4, 6, 5, 7, 6, 5, 3, 5, 6, 7, 5, 3, 2, 1, 2),
(3, 1, 6, 3, 2, 3, 4, 3, 4, 7, 6, 4, 3, 2, 1, 7, 6, 5, 1),
(2, 5, 4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4, 6, 5, 4, 3, 4),
(3, 7, 2, 4, 3, 4, 3, 4, 3, 4, 7, 5, 7, 3, 2, 1, 2),
(1, 6, 5, 6, 7, 5, 6, 7, 5, 6, 3, 2, 1, 4, 5, 3),
(4, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1, 3, 7, 6, 1),
(2, 6, 5, 7, 6, 5, 7, 6, 5, 6, 4, 5, 2, 3),
(1, 4, 3, 4, 3, 4, 3, 4, 3, 7, 2, 1, 4),
(5, 2, 1, 2, 1, 2, 1, 2, 1, 5, 3, 5),
(3, 5, 4, 5, 6, 4, 5, 3, 4, 6, 2),
(1, 2, 3, 1, 3, 2, 1, 5, 2, 1)
])


# n = 7
trials = 400
improvements = 2000
old_score = 0

while True:
    hex_improve(original, improvements, 6, 0)
    break

# node_map = hex_grid_graph.hex_grid(7)
# node_map.print_submission()

#
# n = 8
# trials = 1
# improvements = 10000
#
#
# first = True
# best_score = 0
# #
# while True:
#
#     t1 = time.time()
#     # gets a decent grid for improve to mess around with
#     # original = test3.fill_ones(n, trials)
#     original = hex_grid_graph.hex_grid.create_from_2d_list(
#         [[2, 1, 2, 1, 2, 1, 2, 1],
#          [3, 5, 7, 6, 5, 7, 6, 5, 3],
#          [1, 4, 3, 4, 3, 4, 3, 4, 3, 2],
#          [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
#          [3, 5, 7, 6, 5, 7, 6, 5, 7, 6, 5, 3],
#          [1, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 1],
#          [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
#          [3, 5, 7, 6, 5, 7, 6, 5, 7, 6, 5, 7, 6, 5, 2],
#          [1, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4],
#          [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
#          [3, 5, 7, 6, 5, 7, 6, 5, 7, 6, 5, 3],
#          [1, 4, 3, 4, 3, 4, 3, 4, 3, 4, 2],
#          [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
#          [1, 2, 1, 2, 1, 2, 1, 2, 1],
#          [1, 4, 3, 4, 3, 4, 3, 1]])
#
#     best_score = max(original.calculate_score(), best_score)
#     t2 = time.time()
#     # print("new original: " + str(t2 - t1))
#     temp_best_score = 0
#
#     if first:
#         print(original.calculate_score())
#         original.print_submission()
#         print()
#     first = False
#
#     for i in range(improvements):
#
#         numRows = random.randint(0, 2 * n - 1)
#         offset = 0
#         if numRows < 2 * n - 2:
#             offset = random.randint(0, 2 * n - 2 - numRows)
#
#         node_map = copy.copy(original)
#         node_grid = node_map.get_node_grid()
#
#         nodes_to_fuck_up = []
#         for j in range(numRows):
#             nodes_to_fuck_up.extend(node_grid[j + offset])
#         nodes_to_fuck_up = [node for node in nodes_to_fuck_up if node is not None]
#
#         simplify_area(nodes_to_fuck_up)
#         random_greedy(nodes_to_fuck_up)
#
#         if node_map.calculate_score() > temp_best_score:
#             temp_best_score = node_map.calculate_score()
#             original = node_map
#             #print(str(i) + " " + str(temp_best_score))
#             if temp_best_score > best_score:
#                 best_score = temp_best_score
#                 print("IMPROVED: " + str(numRows + 1) + " " + str(offset) + " " + str(i))
#                 print(node_map.calculate_score())
#                 node_map.print_submission()
#                 print()
#
#     # print("improvements done: " + str(time.time() - t2))
# #
# # node_map.print_submission()
