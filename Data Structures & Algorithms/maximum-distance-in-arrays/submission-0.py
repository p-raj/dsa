class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # lists are already sorted
        # we sort the list by their first item
        A = sorted(arrays, key=lambda x: x[0])
        return abs(A[0][0]-A[-1][-1])