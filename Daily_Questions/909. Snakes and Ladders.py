class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def getPos(pos: int) -> (int, int):
            row = (pos - 1) // n
            col = (pos - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            row = n - 1 - row
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (position, moves)
        while queue:
            pos, moves = queue.popleft()
            for i in range(1, 7):
                newPos = pos + i
                if newPos > n * n:
                    break
                r, c = getPos(newPos)
                if board[r][c] != -1:
                    newPos = board[r][c]
                if newPos == n * n:
                    return moves + 1
                if newPos not in visited:
                    visited.add(newPos)
                    queue.append((newPos, moves + 1))
        
        return -1
