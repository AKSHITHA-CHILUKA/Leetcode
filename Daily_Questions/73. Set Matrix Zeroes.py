from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # Check if the first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Check if the first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Use the first row and first column to mark zeroes
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the first column
                    matrix[0][j] = 0  # Mark the first row
        
        # Set matrix cells to zero based on the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set the first row to zero if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Set the first column to zero if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
