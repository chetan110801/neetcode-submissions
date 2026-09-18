class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.exploreGrid(grid, r, c, visited):
                    count += 1
        return count

    def exploreGrid(self, grid, r, c, visited):
        if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or grid[r][c] == '0' or (r, c) in visited:
            return False

        visited.add((r, c))
        
        self.exploreGrid(grid, r + 1, c, visited)
        self.exploreGrid(grid, r - 1, c, visited)
        self.exploreGrid(grid, r, c + 1, visited)
        self.exploreGrid(grid, r, c - 1, visited)

        return True

        