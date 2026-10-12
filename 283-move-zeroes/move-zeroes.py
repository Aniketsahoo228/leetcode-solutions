class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        next_position = 0  # Position for the next non-zero number

        for current_index in range(len(nums)):  # Check each element
            if nums[current_index] != 0:  # Skip zeroes
                nums[next_position] = nums[current_index]  # Move non-zero forward
                next_position += 1  # Update the next position

        while next_position < len(nums):  # Fill remaining positions with zeroes
            nums[next_position] = 0
            next_position += 1