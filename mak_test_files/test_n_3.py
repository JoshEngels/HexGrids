import time

from tqdm import tqdm






def is_valid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            need = {num: True for num in range(1, grid[y][x])}
            for dif in [(-1, -1), (0, -1),
                        (1, 0), (-1, 0),
                        (0, 1), (1, 1)]:
                try:
                    if ((x+dif[0] >= 0) and (y+dif[1] >= 0)):
                        need[grid[y+dif[1]][x+dif[0]]] = False
                except:
                    None
            if sum(need.values()) > 0:
                return False
    return True


def make_lines(length):
    lines = [[]]
    new_lines = []
    for x in range(length):
        for i in range(1, 8):
            for line in lines:
                new_line = list(line)
                new_line.append(i)
                new_lines.append(new_line)
        lines = new_lines
        new_lines = []
    return lines


def itter_grids():
    size_3 = make_lines(2)
    size_4 = make_lines(3)

    max_score = 0
    best_grid = []

    for first_line in tqdm(size_3):
        for second_line in size_4:
            for third_line in size_3:
                temp = [0]
                temp.extend(third_line)
                third_line = temp
                grid = [first_line,
                        second_line,
                        third_line]
                if is_valid(grid):
                    score = sum([sum(line) for line in grid])
                    if score > max_score:
                        max_score = score
                        best_grid = grid

    print("The highest score was:", max_score)
    print("The best grid was:", best_grid)

    return max_score, best_grid


itter_grids()

# print(is_valid([[3, 2], [4, 1, 4], [0, 2, 3]]))