class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        l = {}
        for k in nums:
            if k not in l:
                l[k] = 1
            else:
                l[k] += 1   

        for k in l:
            if l[k] > n // 2:
                return k         

            
