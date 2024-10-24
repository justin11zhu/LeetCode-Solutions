#https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    result.append((i, board[i][j]))
                    result.append((board[i][j], j))
                    result.append((i // 3, j // 3, board[i][j]))
        return len(result) == len(set(result))

