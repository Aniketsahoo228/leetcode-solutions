from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        top = '.' * n                  # first row: all free
        rest = '#' * (n - 1) + '.'     # other rows: only the last column is free
        return [top] + [rest] * (m - 1)