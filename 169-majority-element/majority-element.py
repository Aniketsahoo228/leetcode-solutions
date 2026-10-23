
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Approach:
        1. Find the length of nums and store it in n.
        2. Create an empty dictionary l to store each number and its frequency.
        3. Traverse nums using a for loop.
        4. If a number is not present in l, initialize its count to 1.
        5. If the number already exists in l, increment its count by 1.
        6. Traverse the dictionary to check the frequency of each number.
        7. If a number appears more than n // 2 times, return that number.
        """

        n = len(nums)  # Store the length of nums
        l = {}  # Store numbers and their frequencies

        for k in nums:  # Traverse each number in nums
            if k not in l:  # Check if the number is new
                l[k] = 1  # Initialize its frequency to 1
            else:
                l[k] += 1  # Increment its frequency

        for k in l:  # Traverse the dictionary keys
            if l[k] > n // 2:  # Check for the majority element
                return k  # Return the majority element
