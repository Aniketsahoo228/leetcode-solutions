class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for items in nums:
            ans.append(nums[items])
        return ans        
        