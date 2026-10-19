class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, ocean, prev_height):
            # base case
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or heights[r][c] < prev_height or (r, c) in ocean:
                return 

            ocean.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, ocean, heights[r][c])

        pacific, atlantic = set(), set()

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])


        return list(pacific.intersection(atlantic))