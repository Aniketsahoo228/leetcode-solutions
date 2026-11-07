class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Remove trailing spaces from the end of the string
        s = s.rstrip()
        
        # Step 2: Find the last space character
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            length += 1
            
        return length