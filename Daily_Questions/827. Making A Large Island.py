class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def explore_land(start): 
            queue = [start] # land cells to explore
            water = set() # all water cells connected to land
            area = 1 # total area of island

            while queue:
                i, j = queue.pop()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj # adjacent cell to land
                    if 0 <= ni < m and 0 <= nj < n: # check if in bounds
                        if grid[ni][nj] == 1: # found land
                            grid[ni][nj] = -1 # set land to visited
                            queue.append((ni,nj)) 
                            area += 1 
                        elif grid[ni][nj] == 0: # found water
                            water.add((ni,nj))
            
            for cell in water: # add island area to water cells
                water_area[cell] += area

        m, n= len(grid), len(grid[0]) 
        water_area = defaultdict(int) # area for each water cell, (water cell): area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: # found unvisited land
                    grid[i][j] = -1 # set land to visited
                    explore_land((i,j))

        if water_area:
            return 1 + max(water_area.values()) # max land connected to water + 1 for water

        return 1 if grid[0][0] == 0 else m*n # edge case for if all cells are water or land
