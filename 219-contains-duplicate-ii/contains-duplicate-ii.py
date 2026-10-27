
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Approach:
        1. Create an empty set called window to store elements in the
           current sliding window.
        2. Traverse nums using a for loop and index i.
        3. If i > k, remove the element that falls outside the window
           using nums[i - k - 1].
        4. Check whether nums[i] already exists in the set.
        5. If it exists, return True because a duplicate is found
           within distance k.
        6. Otherwise, add nums[i] to the set.
        7. If the loop finishes without finding a duplicate, return False.
        """

        window = set()  # Store elements in the current window

        for i in range(len(nums)):  # Traverse nums using index i
            if i > k:  # Check whether an element leaves the window
                window.remove(nums[i - k - 1])  # Remove the element outside the window

            if nums[i] in window:  # Check whether the current element is a duplicate
                return True  # A nearby duplicate exists

            window.add(nums[i])  # Add the current element to the window

        return False  # No nearby duplicate was found
