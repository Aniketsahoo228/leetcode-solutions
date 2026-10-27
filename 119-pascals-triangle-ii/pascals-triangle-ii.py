class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """
        Approach:
        1. Create an empty triangle to store all rows.
        2. Use a loop to generate rows from index 0 to rowIndex.
        3. Initialize each row with 1s because the first and last elements are always 1.
        4. Use the previous row to calculate the middle elements by adding adjacent elements.
        5. Append each completed row to the triangle.
        6. Return the row at the given rowIndex.
        """
        triangle = []  # Store all rows of Pascal's Triangle

        for i in range(rowIndex + 1):  # Generate rows up to rowIndex
            row = [1] * (i + 1)  # Initialize the row with 1s

            for j in range(1, i):  # Calculate only the middle elements
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Add adjacent elements from the previous row

            triangle.append(row)  # Add the completed row to the triangle

        return triangle[rowIndex]  # Return the required row