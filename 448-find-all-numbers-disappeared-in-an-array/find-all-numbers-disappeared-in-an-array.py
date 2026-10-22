
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Approach:
        1. Find the length of nums and store it in n.
        2. Convert nums into a set to store unique elements for
           faster membership checking.
        3. Initialize an empty result list to store missing numbers.
        4. Start checking numbers from 1 using i = 1.
        5. Traverse all numbers from 1 to n using a while loop.
        6. If i is not present in the set, append it to result.
        7. Increment i to check the next number.
        8. Return result containing all missing numbers.
        """

        n = len(nums)  # Store the length of nums
        arr = set(nums)  # Store unique numbers for quick lookup
        result = []  # Store the missing numbers

        i = 1  # Start from the first expected number
        while i <= n:  # Check every number from 1 to n
            if i not in arr:  # Check whether the number is missing
                result.append(i)  # Add the missing number to result
            i += 1  # Move to the next number

        return result  # Return all missing numbers
