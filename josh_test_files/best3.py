# make it so you don't need to check if it will work, because you only fill ones that would

generate_map = {}

def generate_all_new(first, length_this, length_last, needs, max_value):
    if length_this == 0:
        return [[]]

    key = str(length_this) + " " + str(length_last) + str(needs) + str(max_value)
    if length_this < length_last:
        key += str(first)

    if key in generate_map:
        return list(generate_map[key])

    if not needs:
        future_needs = {}
    else:
        future_needs = {index - 1: need for (index, need) in needs.items() if index > 0}

    one_step_down = generate_all_new(False, length_this - 1, length_last - 1, future_needs, max_value)

    result = []
    for i in range(1, max_value + 1):
        for toAdd in one_step_down:
            temp = list(toAdd)
            temp.insert(0, i)

            if length_last < length_this:
                if 0 in needs:
                    need = set(needs[0])
                    need.discard(temp[0])
                    need.discard(temp[1])
                    if not not need:
                        continue

            else:
                if first and 0 in needs:
                    need = set(needs[0])
                    need.discard(temp[0])
                    if not not need:
                        continue

                if 1 in needs:
                    need = set(needs[1])
                    need.discard(temp[0])
                    if len(temp) > 1:
                        need.discard(temp[1])
                    if not not need:
                        continue

            result.append(temp)

    generate_map[key] = result

    return result


#memoize this not anymore
def generate_all_old(index, length_this, max_value, length_last, needs):


    if index == length_this:
        return [[]]

    result = []
    one_step_down = generate_all_old(index + 1, length_this, max_value, length_last, needs)

    for i in range(1, max_value + 1):
        for toAdd in one_step_down:
            temp = list(toAdd)
            temp.insert(0, i)

            if length_last < length_this:
                if index < length_this - 1 and index in needs:
                    need = set(needs[index])
                    need.discard(temp[0])
                    need.discard(temp[1])
                    if not not need:
                        continue

            else:
                if index + 1 in needs:
                    need = set(needs[index + 1])
                    need.discard(temp[0])
                    if len(temp) > 1:
                        need.discard(temp[1])
                    if not not need:
                        continue

                if index == 0 and index in needs:
                    need = set(needs[index])
                    need.discard(temp[0])
                    if not not need:
                        continue

            result.append(temp)

    return result


# needs is a dictionary describing needs: (index, required values)
def generate_needs(last_row, current_row):

    needs = {}
    for index, value in enumerate(current_row):
        surrounding = []

        if len(last_row) > len(current_row):
            surrounding.append(last_row[index])
            surrounding.append(last_row[index + 1])
            if index > 0:
                surrounding.append(current_row[index - 1])
            if index < len(current_row) - 1:
                surrounding.append(current_row[index + 1])

        else:
            if index > 0:
                surrounding.append(current_row[index - 1])
                surrounding.append(last_row[index - 1])
            if index < len(current_row) - 1:
                surrounding.append(last_row[index])
                surrounding.append(current_row[index + 1])

        surrounding = set([num for num in surrounding if num < value])
        if len(surrounding) != value - 1:
            this_needs = set([])
            for i in range(1, value):
                if i not in surrounding:
                    this_needs.add(i)
            needs[index] = this_needs

    return needs




best_map = {}
min_row = 100
rows_seen = set([])

def generate_best(last_row, needs, row_num, row_lengths):

    best_sum = float("-inf")
    best_rows = []

    key = str(last_row) + str(needs) + str(row_num)
    if key in best_map:
        return best_map[key][0], list(best_map[key][1])

    all_possible = generate_all_new(True, row_lengths[row_num], row_lengths[row_num - 1], needs, 7)
    #all_possible = generate_all_old(0, row_lengths[row_num], 7, row_lengths[row_num - 1], needs)
    for current_row in all_possible:

            global min_row
            if row_num <= min_row and row_num in rows_seen:
                min_row = row_num
                print(current_row)
                #print(len(best_map))
            rows_seen.add(row_num)

            new_needs = generate_needs(last_row, current_row)

            impossible = False
            for individual_needs in new_needs.values():
                if len(individual_needs) > 2:
                    impossible = True
                    break
            if impossible:
                continue

            if row_num == len(row_lengths) - 1:
                if not new_needs:
                    if sum(current_row) > best_sum:
                        best_sum = sum(current_row)
                        best_rows = [current_row]

            else:
                test_sum, test_rows = generate_best(current_row, new_needs, row_num + 1, row_lengths)
                test_rows.append(current_row)
                test_sum += sum(current_row)
                if test_sum > best_sum:
                    best_rows = test_rows
                    best_sum = test_sum

    best_map[key] = best_sum, list(best_rows)

    return best_sum, list(best_rows)



needies = generate_needs([1,3,2,4], [4,5,1])

#print(needies)
#print(generate_all_old(0, 2, 7, 3, needies))
#print(generate_all_new(True, 2, 3, needies, 7))


import time

t0 = time.time()
#n=2
#print(generate_best([10], [], 1, [1,2,3,2]))

#n=3
#print(generate_best([10, 10], [], 1, [2, 3, 4, 5, 4, 3]))

#n=4
print(generate_best([10, 10, 10], [], 1, [3, 4, 5, 6, 7, 6, 5, 4]))
t1 = time.time()
print(t1 - t0)