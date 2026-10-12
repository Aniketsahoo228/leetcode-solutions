class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = []                    # stores each unique number, in the order first found
        value = []                   # collects '_' placeholders for duplicates (not used later)
        count  = 0                   # counts how many unique numbers we have found
        for items in nums:           # go through every number in the input list
            if items not in seen:    # check if this number is new (not stored yet)
                seen.append(items)   # new number, so save it in the unique list
                count += 1           # one more unique number found
            else:
                value.append('_')    # duplicate number, so add a placeholder instead
                
        nums[:count] = seen          # overwrite the first 'count' slots of nums with the unique numbers (in-place edit)
        k = count                    # k is the number of unique elements
        return k                     # return k, since the problem only checks the first k elements