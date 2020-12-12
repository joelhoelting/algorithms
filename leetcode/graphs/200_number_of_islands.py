"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List


def number_of_islands(grid: List[List[str]]) -> int:
    if not len(grid):
        return 0

    num_of_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                num_of_islands += 1
                dfs(grid, row, col)

    print(num_of_islands)
    return num_of_islands


def dfs(grid: List, row: int, col: int):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
        return

    grid[row][col] = "0"
    dfs(grid, row + 1, col)
    dfs(grid, row - 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row, col - 1)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "0", "0", "1", "0"],
    ["1", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "1"]
]

number_of_islands(grid)
