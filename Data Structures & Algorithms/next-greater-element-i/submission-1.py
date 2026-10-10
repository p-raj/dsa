class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        N1 = {k: idx for idx, k in enumerate(nums1)}

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                res[N1[val]] = cur
            if cur in N1:
                stack.append(cur)
        return res