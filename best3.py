
#memoize thisssss
def generate_all(index, length_this, max_value, length_last, needs):


    if index == length_this:
        return [[]]

    result = []
    one_step_down = generate_all(index + 1, length_this, max_value, length_last, needs)

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

needs_map = {}


# needs is a dictionary describing needs: (index, required values)
def generate_needs(last_row, current_row):
    key = list(last_row) + list(current_row)
    if key in needs_map:
        return list(needs_map[key])

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

    needs_map[key] = needs
    return needs




memo = {}

def generate_best(last_row, needs, row_num, row_lengths):

    best_sum = float("-inf")
    best_rows = []

    key = str(last_row) + str(needs) + str(row_num)
    if key in memo:
        return memo[key][0], list(memo[key][1])

    all_possible = generate_all(0, row_lengths[row_num], 7, row_lengths[row_num - 1], needs)
    for current_row in all_possible:
            if row_num == 5:
                print(current_row)

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

    memo[key] = best_sum, list(best_rows)

    return best_sum, list(best_rows)




needies = generate_needs([1,2], [3,3,4])

#print(needies)
#print(generate_all(0, 4, 7, 3, needies))


#print(generate_best([10], [], 1, [1,2,3,2]))
print(generate_best([10, 10], [], 1, [2, 3, 4, 5, 4, 3]))
#print(generate_best([10, 10, 10], [], 1, [3, 4, 5, 6, 7, 6, 5, 4]))