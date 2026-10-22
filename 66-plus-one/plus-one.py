
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Approach:
        1. Traverse the digits list from right to left using a for loop.
        2. Start from the last index and move toward the first index.
        3. If the current digit is less than 9, increment it by 1.
        4. Return the updated digits list because no carry is needed.
        5. If the current digit is 9, change it to 0 and continue
           to the previous digit to handle the carry.
        6. If all digits are 9, add 1 at the beginning of the list.
        7. Return the final digits list.
        """

        for i in range(len(digits) - 1, -1, -1):  # Traverse from right to left
            if digits[i] < 9:  # Check if the digit can be incremented
                digits[i] += 1  # Add 1 to the current digit
                return digits  # Return the updated list

            digits[i] = 0  # Reset 9 to 0 and carry 1 to the left

        return [1] + digits  # Handle the case where all digits are 9
