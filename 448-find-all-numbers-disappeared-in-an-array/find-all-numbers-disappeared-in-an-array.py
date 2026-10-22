class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = set(nums)
        result = []

        i = 1 
        while i <= n:
            if i not in arr:
                result.append(i)
            i += 1
        return result        


