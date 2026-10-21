class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, minutes = 0, 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
     
        deq = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    deq.append((i, j))

        while deq:
            if fresh == 0:
                return minutes
            
            for _ in range(len(deq)):
                r, c = deq.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        deq.append((nr, nc))
                        fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1