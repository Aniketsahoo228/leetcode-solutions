
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Approach:
        1. Initialize a pointer i = 0 to track the next position
           where a valid element should be placed.
        2. Initialize count = 0 to count elements not equal to val.
        3. Traverse every element in nums using a for loop.
        4. If an element is not equal to val, place it at nums[i].
        5. Increment count and i after placing a valid element.
        6. Return count, the number of elements not equal to val.
        7. Modify nums in place without creating an extra array
           or sorting the elements.
        """

        i = 0  # Tracks the next position for a valid element
        count = 0  # Counts elements not equal to val

        for items in nums:  # Traverse each element in nums
            if items != val:  # Check if the element should be kept
                nums[i] = items  # Place the valid element at position i
                count += 1  # Increase the count of valid elements
                i += 1  # Move to the next available position

        return count  # Return the total number of valid elements
