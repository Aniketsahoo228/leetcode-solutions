class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        arr = []
        for row in accounts:
            value = sum(row)
            arr.append(value)
        return max(arr)