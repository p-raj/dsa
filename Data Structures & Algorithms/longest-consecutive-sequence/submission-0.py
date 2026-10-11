class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        strt, end_ = 0, 1
        len_ = len(nums)
        seq_ = [0, 0]
        while end_ < len_:
            temp = strt
            while end_ < len_ and nums[end_] - nums[temp] == 1:
                print(temp, end_, nums[temp], nums[end_])
                temp += 1
                end_ += 1
            print(strt, temp, end_)
            print(nums[strt: end_+1])
            prev = seq_[1] - seq_[0]
            if prev < end_ - strt:
                seq_[0] = strt
                seq_[1] = end_
            strt = temp + 1
            end_ += 1
        print(nums[seq_[0]: seq_[1]])
        return seq_[1] - seq_[0] + 1
