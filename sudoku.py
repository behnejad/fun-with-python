# does not support multi cell choices

class Sudoku:
    def __init__(self, board=None):
        if not isinstance(board, list):
            raise "board is not list"

        if len(board) != 9:
            raise f"len board is not 9"

        for r in board:
            if not isinstance(r, list):
                raise f"{r} is not list"

            if len(r) != 9:
                raise f"len {r} is not 9"

            for e in r:
                if not isinstance(e, int):
                    raise f"{e} is not int"

                if not 0 <= e <= 9:
                    raise f"0 <= {e} <= 9"

        self.board = board

    @staticmethod
    def is_num_set_ok(nums):
        if 0 in nums:
            return False
        elif len(nums) < 9:
            return False
        else:
            return True

    def is_cube_ok(self, x, y):
        x *= 3
        y *= 3

        nums = set()
        for i in range(3):
            for j in range(3):
                nums.add(self.board[x + i][y + j])

        return Sudoku.is_num_set_ok(nums)

    def is_row_ok(self, x):
        nums = set()

        for e in self.board[x]:
            nums.add(e)

        return Sudoku.is_num_set_ok(nums)

    def is_column_ok(self, x):
        nums = set()

        for e in range(9):
            nums.add(self.board[e][x])

        return Sudoku.is_num_set_ok(nums)

    def is_complete(self):
        for r in self.board:
            for e in r:
                if e == 0:
                    return False

        for x in range(3):
            for y in range(3):
                if not self.is_cube_ok(x, y):
                    return False

        for x in range(9):
            if not self.is_row_ok(x):
                return False

            if not self.is_column_ok(x):
                return False

        return True

    def solve_cube(self, x, y):
        orgx = x
        orgy = y
        cube_items = set()

        x -= x % 3
        y -= y % 3
        dic = {}

        for i in range(3):
            for j in range(3):
                cell = self.board[x + i][y + j]
                cube_items.add(self.board[x + i][y + j])
                if cell == 0:
                    d = set()
                    for z in range(9):
                        d.add(self.board[x + i][z])
                        d.add(self.board[z][y + j])
                    d.remove(0)
                    dic[f"{x + i},{y + j}"] = d

        cube_items.remove(0)
        d = dic.pop(f"{orgx},{orgy}")

        for z in range(1, 10):
            if z not in cube_items and z not in d:
                for k in dic:
                    if z not in dic[k]:
                        break
                else:
                    # print(f"{orgx}{orgy} => {z}")
                    self.board[orgx][orgy] = z
                    return True

        return False

    def single_move(self):
        moves = 0
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == 0 and self.solve_cube(x, y):
                    moves += 1

        return moves > 0

    def solve(self):
        while not self.is_complete():
            if not self.single_move():
                print("more than one move")
                break

        print("+-------------------+")
        for r in self.board:
            print("| ", end='')
            for e in r:
                print(f"{e} ", end='')
            print("|")
        print("+-------------------+")


game = [[0, 0, 0, 0, 8, 0, 2, 0, 0],
        [7, 4, 0, 6, 0, 0, 0, 5, 0],
        [2, 8, 0, 0, 0, 0, 0, 1, 9],
        [3, 0, 5, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 1, 8, 7, 0, 5],
        [4, 0, 0, 3, 0, 0, 6, 9, 0],
        [0, 0, 0, 0, 0, 6, 9, 2, 0],
        [0, 2, 4, 5, 0, 0, 0, 6, 0],
        [0, 9, 3, 0, 4, 0, 0, 0, 1]]

if __name__ == "__main__":
    s = Sudoku(game)
    s.solve()
