class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.exploreGrid(grid, r, c, visited)
                if size > max_area:
                    max_area = size
        return max_area

    def exploreGrid(self, grid, r, c, visited):
        if not 0<=r<len(grid) or not 0<=c<len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
            return 0
        visited.add((r, c))
        size = 1
        size += self.exploreGrid(grid, r + 1, c, visited)
        size += self.exploreGrid(grid, r - 1, c, visited)
        size += self.exploreGrid(grid, r, c + 1, visited)
        size += self.exploreGrid(grid, r, c - 1, visited)
        return size