class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        min_heap = [(grid[0][0], 0, 0)]

        visited = set()
        visited.add((0,0))

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == N - 1 and c == N -1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))
                    visited.add((nr, nc))
