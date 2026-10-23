class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Approach:
        1. Find the length of nums and store it in n.
        2. Create a list hasht of size n + 1, initialized with zeros.
        3. Traverse nums and mark each present number with 1 in hasht.
        4. Traverse numbers from 1 to n.
        5. If hasht[k] is 0, the number k is missing from nums.
        6. Append each missing number to the result list l.
        7. Return l containing all missing numbers.
        """

        n = len(nums)  # Store the length of nums
        l = []  # Store the missing numbers
        hasht = [0] * (n + 1)  # Initialize presence markers

        for k in nums:  # Visit each number in nums
            hasht[k] = 1  # Mark the number as present

        for k in range(1, n + 1):  # Check numbers from 1 to n
            if hasht[k] == 0:  # Check if the number is missing
                l.append(k)  # Add the missing number to l

        return l  # Return the missing numbers