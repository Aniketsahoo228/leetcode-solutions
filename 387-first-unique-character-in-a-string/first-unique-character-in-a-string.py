class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in s:
            seen[i] = seen.get(i , 0) + 1 # Count each character


        for index , values in enumerate(s):
            if seen[values] == 1:  # Count each character

                return index # Count each character

        return -1            
        
