class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        value = []
        for items in nums1:
            if items in nums2 :
                if items not in value:
                    value.append(items)
        return value
