import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_ = len(nums)
        if len_ == 0:
            return 0
        if len_ == 1:
            return 1
        if len_ == 2:
            return 1 if abs(nums[1] - nums[0]) != 1 else 2
        # can't sort -> work to be done in O(n)
        numd = dict()
        min_ = math.inf
        for num in nums:
            numd[num] = None
            if num < min_:
                min_ = num
        
        longest_seq = 1
        while True:
            next_ = min_ + 1
            sequence_count = 1
            while next_ in numd:
                numd.pop(min_, None)
                sequence_count += 1
                min_ = next_
                next_ = min_ + 1
            if sequence_count > longest_seq:
                longest_seq = sequence_count
            if not numd:
                break
            numd.pop(min_, None)
            # next min?
            min_ = math.inf
            for num in numd:
                if num < min_:
                    min_ = num
        return longest_seq