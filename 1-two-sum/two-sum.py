class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # I have used Brute force Approach
        for i in range(len(nums)):
            val = target- nums[i]
            if val in nums:
                j = nums.index(val)
                if j != i:
                    return [i,j]

