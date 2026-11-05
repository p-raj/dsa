class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        len_ = len(arr)
        min_lft = [-1] * len_
        min_rgt = [len_] * len_

        stack = []
        for idx, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                min_rgt[stack.pop()] = idx
            stack.append(idx)

        stack = []
        for idx in range(len_):
            while stack and arr[stack[-1]] > arr[idx]:
                stack.pop()
            if stack:
                min_lft[idx] = stack[-1]
            else:
                min_lft[idx] = -1
            stack.append(idx)

        ans = 0
        # [...(i)...(n)]
        # any ith min node would contribute to
        # (i) * (n-i) * cost(i)
        # print(min_rgt)
        # print(min_lft)
        for i in range(len_):
            ans += (i - min_lft[i]) * (min_rgt[i] - i) * arr[i]
        return ans % (10**9 + 7)
