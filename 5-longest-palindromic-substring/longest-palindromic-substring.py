class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length of palindrome found
        
        for i in range(len(s)):
            # Odd length palindromes (single center, e.g., "aba")
            len1 = expandAroundCenter(i, i)
            # Even length palindromes (double center, e.g., "abba")
            len2 = expandAroundCenter(i, i + 1)
            
            max_len = max(len1, len2)
            if max_len > end - start + 1:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]