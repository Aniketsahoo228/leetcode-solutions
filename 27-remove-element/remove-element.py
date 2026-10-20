class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        first make an empty arr  
        then we will remove element of the arr
        then we woll sort it and give the lenght of th value
        """

        i = 0 
        count  = 0
        for items in nums:
            if items != val:
                nums[i] = items
                count += 1
                i += 1
        return count        



