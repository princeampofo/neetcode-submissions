class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Understand the problem 
        # Input = 2D array of containing 1 and 0 in string
        # Output = Integer representing the number of islands
        # No invalid inputs

        # Plan
        # Can be solved with dfs or bfs
        # Preferably code the dfs
        # 1. Loop through the 2D grid
        # 2. If the value is a '1' run a dfs to find how many other 1's its connected 
        # to whilst setting every encountered 1 to 0. We can use a visited set but this is easier. Skip if zero
        # 3. One the dfs terminates, add 1 to the overall results as an island was formed
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        no_of_islands = 0
        # def dfs(r, c):
        #     # base case
        #     if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or grid[r][c] == "0":
        #         return 

        #     grid[r][c] = "0"
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)
           
        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()
                grid[row][col] = 0
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    no_of_islands += 1


        return no_of_islands

        






        