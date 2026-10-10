class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        rgt1 = m - 1
        rgt2 = n - 1

        while rgt2 >= 0:
            if rgt1 >= 0 and nums1[rgt1] > nums2[rgt2]:
                nums1[last] = nums1[rgt1]
                rgt1 -= 1
            else:
                nums1[last] = nums2[rgt2]
                rgt2 -= 1
            last -= 1
