class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        N2 = {
            v:idx for idx, v in enumerate(nums2)
        }
        gt2 = [-1] * len(nums2)
        n2stack = []
        for i2, n2 in enumerate(nums2):
            while n2stack and nums2[n2stack[-1]] < n2:
                gt2[n2stack.pop()] = n2
            n2stack.append(i2)

        # find the index j such that nums1[i] == nums2[j]
        for n1 in nums1:
            i2 = N2[n1]
            ans.append(gt2[i2])
        return ans