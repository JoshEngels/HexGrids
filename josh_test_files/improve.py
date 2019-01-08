import hex_grid_graph
# import mak_test_files.test_n_3 as test3
import random
import copy


def simplify_area(node_list):
    for value_to_decrement in range(7, 1, -1):
        for node in node_list:
            if node.get_value() == value_to_decrement:
                node.try_decrement()


# DAMN THAT WAS DUMB. NEED TO COMMENT IN COMMIT
# Maybe going out from the center was good?
# Maybe need to use resets for this method
# Honestly I don't know if random greedy is the best
def random_greedy(node_list):
    did_increment = True

    while did_increment:
        did_increment = False

        for _ in range(len(node_list)):
            n = random.choice(node_list)
            if n.try_increment():
                did_increment = True

        if not did_increment:
            for node in node_list:
                if node.try_increment():
                    did_increment = True
                    break


def random_greedy2(node_list):
    did_increment = True

    while did_increment:
        did_increment = False
        for node in node_list:
            if node.try_increment():
                did_increment = True


def random_greedy3(node_list):
    did_increment = True

    while did_increment:
        did_increment = False
        for node in node_list:
            while node.try_increment():
                did_increment = True


def update_without_regard(nodes):
    simplify_area(nodes)
    random_greedy2(nodes)


def update(graph, nodes):
    old = copy.copy(graph)
    change = True

    simplify_area(nodes)
    random_greedy(nodes)

    if old.calculate_score() >= graph.calculate_score():
        graph = old
        change = False

    return graph, change


def hex_improve(graph, runs_through_the_graph, max_hex_size, best_score_so_far):
    """
    Loops through every element in the graph multiple times and tries to improve hexes from size 1 to max_hex_size
    at every one of those elements
    :param graph: The graph to attempt to improve
    :param runs_through_the_graph: The number of times to loop through every element in the graph after changes stop.
    :param max_hex_size: The max hex size to test
    :param best_score_so_far: The best score attained for this n so far. The function will print
    out scores found greater than this score, as well as grids.
    :return: The graph, improved if possible or otherwise the same
    """

    counter = 0
    while counter < runs_through_the_graph:
        counter += 1
        for i in range(len(graph.get_node_list())):
            for j in range(1, max_hex_size + 1):

                node_list = graph.get_node_list()
                graph, change = update(graph, hex_grid_graph.hex_grid.get_hex(node_list[i], j))

                if graph.calculate_score() > best_score_so_far:
                    print(str(i) + " " + str(j) + " " + str(counter))
                    best_score_so_far = graph.calculate_score()
                    print(best_score_so_far)
                    graph.print_submission()
                    print()

                if change:
                    counter = 0

    return graph


# original = hex_grid_graph.hex_grid.create_from_2d_list([

#
# n = 20
# trials = 50
# improvements_to_wait = 5
# old_score = 0
#
# while True:
#     grid = test3.fill_ones(n, trials)
#     # grid = hex_grid_graph.hex_grid(n)
#     new_score = hex_improve(grid, improvements_to_wait, 3, old_score).calculate_score()
#     old_score = max(old_score, new_score)

grid = ((4, 3, 5, 4, 3, 4, 5, 3, 5, 4, 3, 2),
        (2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 3),
        (3, 5, 4, 3, 7, 6, 5, 4, 3, 4, 7, 5, 4, 5),
        (1, 7, 6, 1, 5, 4, 3, 7, 6, 5, 6, 3, 6, 2, 1),
        (5, 4, 2, 3, 6, 2, 1, 2, 1, 2, 1, 2, 1, 7, 4, 3),
        (2, 3, 1, 5, 7, 4, 6, 7, 3, 5, 4, 4, 6, 3, 5, 6, 2),
        (1, 5, 6, 4, 2, 1, 3, 5, 4, 7, 6, 3, 5, 2, 1, 2, 1, 2),
        (2, 4, 2, 1, 3, 5, 6, 2, 1, 2, 1, 2, 1, 7, 6, 5, 4, 3, 4),
        (1, 1, 3, 5, 6, 4, 1, 4, 3, 4, 6, 7, 4, 3, 4, 3, 7, 6, 5, 1),
        (3, 5, 2, 4, 7, 2, 6, 5, 7, 6, 5, 3, 5, 7, 2, 1, 2, 1, 2, 4, 3),
        (2, 4, 7, 6, 1, 3, 1, 3, 2, 1, 2, 1, 2, 1, 6, 5, 3, 4, 6, 7, 5, 2),
        (1, 6, 1, 3, 5, 4, 6, 5, 4, 1, 5, 4, 3, 4, 3, 4, 7, 6, 5, 3, 1, 6, 1),
        (3, 5, 7, 2, 6, 2, 1, 2, 5, 3, 7, 6, 5, 6, 2, 1, 2, 1, 2, 5, 4, 3),
        (2, 4, 6, 1, 3, 6, 4, 7, 6, 2, 1, 2, 1, 7, 3, 5, 4, 3, 7, 1, 2),
        (1, 3, 5, 4, 5, 2, 3, 1, 4, 6, 5, 3, 5, 4, 7, 6, 1, 6, 4, 3),
        (2, 6, 2, 6, 1, 4, 6, 5, 3, 7, 4, 6, 2, 1, 2, 3, 5, 2, 5),
        (4, 1, 7, 3, 5, 7, 2, 1, 2, 1, 2, 1, 6, 5, 4, 1, 4, 1),
        (3, 4, 5, 2, 1, 3, 6, 5, 7, 6, 5, 4, 3, 7, 6, 3, 5),
        (2, 1, 3, 4, 5, 7, 4, 3, 4, 3, 7, 2, 1, 2, 5, 2),
        (4, 5, 7, 6, 2, 1, 2, 1, 2, 1, 6, 3, 7, 4, 1),
        (3, 2, 1, 3, 5, 4, 6, 5, 3, 5, 4, 6, 5, 3),
        (1, 5, 4, 7, 6, 3, 7, 4, 2, 1, 2, 1, 2),
        (3, 2, 1, 2, 1, 2, 1, 5, 3, 5, 4, 3)
        )

grid = hex_grid_graph.hex_grid.create_from_2d_list(grid)
hex_improve(grid, 1000, 4, 0)

# (4, 2, 1, 5, 4, 3, 2),
# (1, 3, 4, 3, 2, 1, 1, 2),
# (4, 6, 5, 6, 7, 4, 6, 5, 3),
# (3, 2, 1, 2, 1, 5, 3, 2, 4, 1),
# (1, 4, 7, 5, 4, 2, 7, 1, 6, 5, 2),
# (2, 2, 6, 3, 1, 3, 6, 4, 1, 3, 6, 4),
# (3, 1, 4, 2, 6, 5, 2, 1, 1, 2, 7, 1, 3),
# (1, 6, 5, 7, 4, 1, 6, 4, 6, 5, 4, 2),
# (2, 3, 1, 3, 2, 5, 3, 2, 3, 1, 3),
# (5, 4, 7, 6, 4, 3, 1, 5, 4, 5),
# (1, 2, 5, 1, 7, 2, 6, 7, 2),
# (4, 3, 4, 5, 6, 4, 3, 1),
# (2, 1, 2, 3, 1, 5, 2)


# Follow different paths along same tree, can get stuck in holes even with this strategy too, good grids
# a far way apart from each other so not much to learn from each other it seems and also can get stuck
# Simulated annealing? --> switch two, make it work with decrementing, then greedy? Maybe not switching could
# just be decreasing than increasing like here but instead of always taking better only take better sometimes
# alla simulated annealing??? Random neighbors are random hex grid size and random position??? or somehow more
# to make it a better neighbor. Actually not sure. Maybe don't greedy always for neighbor but I don't know what else


# Score could be positive for grids that work, negative for
