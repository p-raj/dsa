class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # a = [1, 2]
        # 0-[1,2], 1-[2], 2-[] 3-[1], 4-[1,2]
        # 2 * size, the array is back to beginning
        res = []
        size = len(nums)
        for time, index in queries:
            time = time % (2 * size)
            if time < size:
                # draining
                len_ = size - time
                index += time
            else:
                # filling
                len_ = time - size

            if index >= len_:
                res.append(-1)
            else:
                res.append(nums[index])

        return res
