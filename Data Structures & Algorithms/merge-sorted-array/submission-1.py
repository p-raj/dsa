
class Solution:
    def bins_idx(self, nums1: List[int], m: int, num: int) -> int:
        lft = 0
        rgt = m
        while lft < rgt:
            mid = (lft + rgt)//2
            if num > nums1[mid]:
                lft = mid + 1
            else:
                rgt = mid
        print(lft, rgt, nums1)
        return lft

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # zero starts at m
        # for each num2 element
        # insert 1 element at a time
        # m increases by 1
        for n2 in nums2:
            idx = self.bins_idx(nums1, m, n2)
            # whereever this gets inserted
            # elements after this needs to shift by 1
            # elements to shift = m - idx
            # given m - idx > 0
            jmp = m - idx
            i = m
            while jmp > 0:
                nums1[i] = nums1[i-1]
                jmp -= 1
                i -= 1
            m += 1
            nums1[idx] = n2
            print(nums1)