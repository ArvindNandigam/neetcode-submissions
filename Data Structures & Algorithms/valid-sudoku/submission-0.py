from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            temp = [x for x in row if x != "."]
            if len(temp) != len(set(temp)):
                return False

        # Check columns
        for col in zip(*board):
            temp = [x for x in col if x != "."]
            if len(temp) != len(set(temp)):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] != ".":
                            box.append(board[r][c])

                if len(box) != len(set(box)):
                    return False

        return True