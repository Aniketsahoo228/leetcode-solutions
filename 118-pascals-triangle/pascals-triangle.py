
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """
        Approach:
        1. Create an empty list triangle to store all rows of Pascal's Triangle.
        2. Use a for loop to generate each row from index 0 to numRows - 1.
        3. Initialize each row with 1s using [1] * (i + 1).
        4. Traverse the inner positions of the current row, excluding
           the first and last elements.
        5. Calculate each inner element by adding the two elements
           directly above it from the previous row.
        6. Append the completed row to triangle.
        7. Return triangle containing all rows of Pascal's Triangle.
        """

        triangle = []  # Store all rows of Pascal's Triangle

        for i in range(numRows):  # Generate each row
            row = [1] * (i + 1)  # Initialize the row with 1s

            for j in range(1, i):  # Calculate the inner elements
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Add the two elements above

            triangle.append(row)  # Add the completed row to triangle

        return triangle  # Return the generated triangle
