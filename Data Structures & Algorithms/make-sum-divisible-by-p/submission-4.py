class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        len_ = len(nums)

        total = sum(nums)
        reminder = total % p
        if reminder == 0:
            return 0

        seen = {0: -1}
        res = len_

        prefix = 0
        # nums = [3, 1, 4, 2]
        # p = 6
        # 10 % 6 = 4
        # So we need to remove something whose remainder is also 4.
        for idx, num in enumerate(nums):
            prefix += num
            # current_prefix - previous_prefix) % p == need
            # previous_prefix % p == (current_prefix - need) % p
            target = (prefix - reminder) % p

            if target in seen:
                length = idx - seen[target]
                res = min(res, length)

            seen[prefix%p] = idx

        return res if res < len_ else -1

        # count = len(prefix)
        # for i in range(len(prefix)):
        #     for j in range(i + 1, len(prefix)):
        #         if (prefix[j] - prefix[i]) % p == reminder:
        #             count = min(count, j - i)
        # return count if count < len_ else -1

        # (a + b) mod m = ((a mod m) + (b mod m)) mod m
        # (a * b) mod m = ((a mod m) * (b mod m)) mod m
        # (a - b) mod m = ((a mod m) - (b mod m) + m) mod m
        # -a (mod m) = m - a

        return 0
