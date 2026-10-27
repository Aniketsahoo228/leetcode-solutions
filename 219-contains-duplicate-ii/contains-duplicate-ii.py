
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Approach:
        1. Convert nums into a set to check whether all elements are unique.
        2. If the set length equals the original list length, return False
           because there are no duplicates.
        3. Create an empty dictionary mp to store each number and its
           most recent index.
        4. Traverse nums using enumerate() to get each index i and value n.
        5. Use mp.get(n) to retrieve the previous index of n, if it exists.
        6. If a previous index exists and the distance between the current
           index and previous index is at most k, return True.
        7. Otherwise, update mp[n] with the current index i.
        8. If no nearby duplicate is found, return False.
        """

        if len(set(nums)) == len(nums):  # Check whether all elements are unique
            return False  # No duplicates exist

        mp = {}  # Store each number and its most recent index

        for i, n in enumerate(nums):  # Get each index and number
            j = mp.get(n)  # Retrieve the previous index, if available

            if j is not None and i - j <= k:  # Check the distance between duplicate indices
                return True  # A nearby duplicate exists

            mp[n] = i  # Update the most recent index of the number

        return False  # No nearby duplicate was found
