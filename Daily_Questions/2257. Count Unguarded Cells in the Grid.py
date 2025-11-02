class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        # Step 1: Initialize the grid
        # 0 → unguarded, 1 → guarded, 2 → occupied (guard or wall)
        grid = [[0] * n for _ in range(m)]

        # Step 2: Mark guards and walls on the grid
        for r, c in guards:
            grid[r][c] = 2
        for r, c in walls:
            grid[r][c] = 2

        # Step 3: Define directions (up, right, down, left)
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Step 4: Simulate guard vision (ray propagation)
        for gr, gc in guards:
            for dr, dc in dirs:
                r, c = gr + dr, gc + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] < 2:
                    grid[r][c] = 1  # mark as guarded
                    r += dr
                    c += dc

        # Step 5: Count unguarded cells
        count = sum(cell == 0 for row in grid for cell in row)

        # Step 6: Return the result
        return count
