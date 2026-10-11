class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_ = len(nums)
        nums.sort()
        if len_ in {0, 1}:
            return 0
        
        if len_ == 2:
            return 1 if nums[1] - nums[0] != 1 else 2

        strt, end_ = 0, 1
        seq_ = [strt, end_]
        while end_ < len_:
            temp = strt
            while end_ < len_ and nums[end_] - nums[temp] == 1:
                print(temp, end_, nums[temp], nums[end_])
                temp += 1
                end_ += 1
            prev = seq_[1] - seq_[0]
            if prev < end_ - strt:
                seq_[0] = strt
                seq_[1] = end_
            strt = temp + 1
            end_ += 1
        return seq_[1] - seq_[0] + 1
