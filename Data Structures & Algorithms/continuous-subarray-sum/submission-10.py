class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # remainder -> earliest index where this remainder occurred
        #
        # remainder 0 exists "before" the array begins.
        # This handles subarrays starting at index 0.
        seen = {0: -1}

        prefix = 0

        for i, num in enumerate(nums):
            prefix = (prefix + num) % k

            if prefix in seen:
                # Subarray is:
                #
                # seen[prefix] + 1 ... i
                #
                # Its length is:
                # i - seen[prefix]
                if i - seen[prefix] >= 2:
                    return True

            else:
                # Keep the EARLIEST occurrence.
                # Earlier index => larger possible subarray.
                seen[prefix] = i

        return False