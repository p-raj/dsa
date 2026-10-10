class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        N2 = {
            k:idx for idx,k in enumerate(nums2)
        }
        for n1 in nums1:
            idx2 = N2[n1]
            res.append(-1)
            while idx2 < len(nums2):
                if nums2[idx2] > n1:
                    res[len(res)-1] = nums2[idx2]
                    break
                idx2 += 1
        return res