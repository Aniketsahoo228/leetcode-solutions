class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        result = []

        for row in matrix:
            value = min(row)
            j = row.index(value)
                 
            if value == max(r[j] for r in matrix) :
                result.append(value)
        return result      