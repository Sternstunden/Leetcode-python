#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (40.67%)
# Likes:    1374
# Dislikes: 82
# Total Accepted:    164.4K
# Total Submissions: 402.2K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# 
# 
# Empty cells are indicated by the character '.'.
# 
# 
# A sudoku puzzle...
# 
# 
# ...and its solution numbers marked in red.
# 
# Note:
# 
# 
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
# 
# 
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return
        self.solve(board, 0, 0)

    def solve(self, board, row, col):
        while board[row][col] != ".":
            col += 1
            if col >= 9:
                row, col = row+1, 0
            if row >= 9:
                return True 
        for i in range(1,10):
            c = str(i)
            if self.isValid(board, row, col, c):
                board[row][col] = c
                if self.solve(board, row, col):
                    return True
        board[row][col] = "."
        return False

    def isValid(self, board, row, col, c):
        base_row = 3*(row//3)
        base_col = 3*(col//3)
        for i in range(0,9):
            if board[i][col] == c or board[row][i] == c or \
                board[base_row+i//3][base_col+i%3] == c:
                return False
        return True
# @lc code=end

