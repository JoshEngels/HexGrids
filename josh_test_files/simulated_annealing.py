import josh_test_files.improve as improve
import hex_grid_graph
import copy
import random
import math


def change_into_neighbor(hex_grid):
    subset = hex_grid.get_random_hex(1, 4)
    improve.update_without_regard(subset)


def acceptance_probability(old, new, temperature):
    if new > old:
        return 1
    else:
        return math.e ** ((new - old) / temperature)


#
# original = hex_grid_graph.hex_grid(7)
# while True:
#     new_graph = copy.copy(original)
#     change_into_neighbor(new_graph)
#
#     if new_graph.calculate_score() > original.calculate_score():
#         original = new_graph


grid = ((2, 1, 2, 4, 3, 2),
        (4, 3, 4, 5, 1, 5, 1),
        (2, 1, 6, 7, 3, 4, 6, 2),
        (4, 3, 5, 2, 1, 2, 7, 3, 4),
        (1, 6, 7, 4, 3, 4, 5, 1, 5, 1),
        (3, 5, 2, 1, 5, 6, 7, 3, 7, 2, 4),
        (2, 4, 3, 6, 2, 1, 2, 4, 6, 3),
        (1, 6, 1, 4, 3, 6, 1, 5, 1),
        (2, 5, 7, 6, 5, 4, 3, 2),
        (4, 3, 2, 1, 2, 4, 5),
        (1, 5, 4, 3, 5, 1)

        )

sol = hex_grid_graph.hex_grid(12)
# sol = hex_grid_graph.hex_grid.create_from_2d_list(grid)
old_score = sol.calculate_score()
best = sol
best_score = sol.calculate_score()
# T = 1
T = 1
T_min = 0.00001
alpha = 0.99
while T > T_min:
    i = 1
    while i <= 500:
        new_sol = copy.copy(sol)
        change_into_neighbor(new_sol)
        new_score = new_sol.calculate_score()
        ap = acceptance_probability(old_score, new_score, T)
        if ap > random.random():
            sol = new_sol
            old_score = new_score
        i += 1

        if new_score > best_score:
            best_score = new_score
            best = sol

    best.print_submission()
    print(str(best_score) + " " + str(T) + " " + str(new_score))
    T = T * alpha

# graph best score vs alpha --> seems like much happens early... actually maybe not idk. Maybe just higher min t
# understand algo
# implement restart to best
# allow less good than full greedy (ie input a number fro, 0 to 1 that says how far to go along with greedy)
# Honestly seems to just range around a lot and find high scores. Should think about that and also maybe start
# good ones with lower starting temperature
# Automate entries lots at once
# randomize order each time for random greedy to truly make it able to reach everything
