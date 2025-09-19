class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = [[0] * 26 for _ in range(rows)]
    
    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.cells[row][col] = value
    
    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)
    
    def getValue(self, formula: str) -> int:
        idx = formula.index('+')
        left = formula[1:idx]
        right = formula[idx+1:]
        
        if left[0].isalpha():
            val_left = self.cells[int(left[1:]) - 1][ord(left[0]) - 65]
        else:
            val_left = int(left)
        
        if right[0].isalpha():
            val_right = self.cells[int(right[1:]) - 1][ord(right[0]) - 65]
        else:
            val_right = int(right)
        
        return val_left + val_right
