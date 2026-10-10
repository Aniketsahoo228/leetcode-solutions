class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        arr = []
        for i in range(len(nums)):
            count = 0 
            for j in range(len(nums)):
                if nums[i] > nums[j] and nums[i]!= nums[j]:
                    count+=1 
            arr.append(count)              
        return arr              
