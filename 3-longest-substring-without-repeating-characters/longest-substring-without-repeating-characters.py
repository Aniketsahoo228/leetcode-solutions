class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        # Loop right pointer through every character in the string
        for right in range(len(s)):
            # If character is already in char_set, remove from left until duplicate is gone
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to set
            char_set.add(s[right])
            
            # Calculate current window size and update max_length
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                
        return max_length