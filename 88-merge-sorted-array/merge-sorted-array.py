
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        # Approach: Three Pointers (Merge from the End)
        # 1. nums1 already has length m + n, with empty slots at the end.
        # 2. i points to the last valid element in nums1.
        # 3. j points to the last element in nums2.
        # 4. k points to the last position in nums1.
        # 5. Compare nums1[i] and nums2[j], and place the larger
        #    element at nums1[k].
        # 6. Move the corresponding pointer backward after placing it.
        # 7. Continue until all elements of nums2 are merged.
        # 8. nums1 is modified in place; no extra array is needed.

        i = m - 1       # Last valid element in nums1
        j = n - 1       # Last element in nums2
        k = m + n - 1   # Last position in nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # Place the larger element
                i -= 1
            else:
                nums1[k] = nums2[j]  # Place the element from nums2
                j -= 1

            k -= 1  # Move to the previous position
