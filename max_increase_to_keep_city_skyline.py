grid = [[3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0]]

import itertools
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        flat = list(itertools.chain(*grid))

        tb = [max(flat[c::cols]) for c in range(cols)]
        lr = [max(grid[r]) for r in range(rows)]

        out = 0
        for r in range(rows):
            for c in range(cols):
                out += min([tb[c], lr[r]]) - grid[r][c]
        return out


if __name__ == '__main__':
    sol = Solution()
    res = sol.maxIncreaseKeepingSkyline(grid)
    print(res)
