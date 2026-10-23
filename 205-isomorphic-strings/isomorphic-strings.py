class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        
        for c1, c2 in zip(s, t):
            # If c1 is already mapped to a different character, return False
            if c1 in map_s_to_t and map_s_to_t[c1] != c2:
                return False
            # If c2 is already mapped to a different character, return False
            if c2 in map_t_to_s and map_t_to_s[c2] != c1:
                return False
            
            # Create the mapping
            map_s_to_t[c1] = c2
            map_t_to_s[c2] = c1
            
        return True