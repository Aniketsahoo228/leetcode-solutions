class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        best_value = window
        for i in range(len(nums) - k):
            window = window - nums[i] + nums[i + k]
            best_value = max(best_value, window)
        return best_value / k