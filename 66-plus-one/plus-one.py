class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        value = int("".join(map(str,digits)))
        new_value = value + 1 
        digits = list(map(int,str(new_value)))
        return digits            