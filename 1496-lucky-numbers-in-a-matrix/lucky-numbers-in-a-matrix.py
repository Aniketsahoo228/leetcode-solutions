class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        true_value = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            value = min(matrix[i])
            j = matrix[i].index(value)       

            col_max = max(matrix[r][j] for r in range(m))
            if value == col_max:
                true_value.append(value)

        return true_value
                 