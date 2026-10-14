class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen1 ={}
        value = 1
        for i in s:
            seen[i] = seen.get(i , 0) + 1
        for j in t:
            seen1[j] = seen1.get(j , 0) + 1
    
        return seen == seen1   