
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1          # Last valid element in nums1
        j = n - 1          # Last element in nums2
        k = m + n - 1      # Last position in nums1

        while j >= 0:      # Continue until nums2 is fully merged
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # Place larger element from nums1
                i -= 1
            else:
                nums1[k] = nums2[j]  # Place element from nums2
                j -= 1

            k -= 1             # Move to the previous position
