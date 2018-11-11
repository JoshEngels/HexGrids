

class HexArray:
    """
    Represents a hex grid as an array padded with zeros, such that a tiles neighbors are
    always the two integers next to them, the ones above them with index the same or minus one,
    and the ones below them with index the same or plus one. Rows above the center padded to the left,
    rows below the center padded to the right. Rows are indexed from bottom to top, columns are index from left
    to right. Left and right padded with a column of all zeros. Just call get and set methods.
    Do not access grid directly.
    """

    def __init__(self, n):
        """
        :param n: The number of hex tiles per side
        """

        self.num_rows = n * 2 - 1
        self.middleRowIndex = self.num_rows // 2

        # size by size array filled initially with 0s
        self.grid = [[0 for _ in range(self.num_rows + 2)] for _ in range(self.num_rows)]

    def __str__(self):
        representation = ""

        for row_index in range(self.num_rows - 1, -1, -1):
            representation += str(tuple(self.get_row(row_index)))
            if row_index != 0:
                representation += ",\n"

        return representation

    def _get_array_col_index(self, row, col):
        return col + 1 if (row > self.middleRowIndex) else (col + 1 + (self.middleRowIndex - row))

    def set(self, row, col, value):
        self.grid[row][self._get_array_col_index(row, col)] = value


    def get(self, row, col):
        try:
            return self.grid[row][self._get_array_col_index(row, col)]
        except IndexError:
            print(col)
            print(row)
            print(self._get_array_col_index(row, col))
            print()

    def get_row(self, row_index):
        if row_index > self.middleRowIndex:
            return self.grid[row_index][1: self.num_rows + 1 - (row_index - self.middleRowIndex)]
        else:
            # -1 because last column is zeros
            return self.grid[row_index][self._get_array_col_index(row_index, 0): -1]

    def get_neighbors(self, row, col):
        other_values = []
        index = self._get_array_col_index(row, col)

        if row > 0:
            other_values.append(self.grid[row - 1][index + 1])
            other_values.append(self.grid[row - 1][index])

        if row < self.num_rows - 1:
            other_values.append(self.grid[row + 1][index - 1])
            other_values.append(self.grid[row + 1][index])

        other_values.append(self.grid[row][index + 1])
        other_values.append(self.grid[row][index - 1])

        return other_values

    def get_neighbors_less_than(self, row, col):
        return set(i for i in self.get_neighbors(row, col) if i in range(1, self.get(row, col)))

    def get_row_length(self, row):
        return len(self.get_row(row))

    def is_valid(self, row, col):
        #print(str(len(self.get_neighbors_less_than(row, col))) + str(self.grid[row][col]))
        return len(self.get_neighbors_less_than(row, col)) == self.get(row,col) - 1

    def valid(self):
        for row in range(self.num_rows):
            for col in range(self.get_row_length(row)):
                if not self.is_valid(row, col):
                    return False
        return True



# Greedy algo
test = HexArray(10)

for row_index in range(test.num_rows):
    for col_index in range(test.get_row_length(row_index)):
        test.set(row_index, col_index, 1)


repeat = True
while repeat:
    repeat = False
    for row_index in range(test.num_rows):
        for col_index in range(test.get_row_length(row_index)):
            while True:
                test.set(row_index, col_index, test.get(row_index, col_index) + 1)
                if not test.valid():
                    test.set(row_index, col_index, test.get(row_index, col_index) - 1)
                    break
                else:
                    repeat = True

print(test)
