class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        # odd:
        #   number of ODD-sum subarrays
        #   ending at the PREVIOUS element
        #
        # even:
        #   number of EVEN-sum subarrays
        #   ending at the PREVIOUS element
        odd = 0
        even = 0

        ans = 0

        for num in arr:

            if num % 2 == 0:
                # Example: num = 2
                #
                # Before 2, from [1]:
                #
                # odd = 1   -> [1]
                # even = 0
                #
                # Append 2:
                #
                # [1] + 2 = [1,2]
                #
                # odd + even = odd
                #
                # So the previous odd subarrays
                # remain odd.
                #
                # We ALSO get the new one-element subarray:
                #
                # [2] -> even
                #
                # Therefore:
                #
                # odd stays the same
                # even gets +1

                even += 1

            else:
                # Example 1: num = 1
                #
                # There are no previous subarrays.
                #
                # But we get:
                #
                # [1] -> odd
                #
                # therefore:
                #
                # new_odd = old_even + 1
                #          = 0 + 1
                #          = 1
                #
                #
                # Example 2: later num = 3
                #
                # Before 3, the subarrays ending at 2 are:
                #
                # [2]   -> EVEN
                # [1,2] -> ODD
                #
                # so:
                #
                # even = 1
                # odd  = 1
                #
                # Append 3:
                #
                # [2]   + 3 = [2,3]
                # EVEN + ODD = ODD
                #
                # [1,2] + 3 = [1,2,3]
                # ODD + ODD = EVEN
                #
                # And we also start fresh:
                #
                # [3] -> ODD
                #
                # Therefore:
                #
                # new odd:
                #     previous EVEN subarrays + [3]
                #
                #     = even + 1
                #     = 1 + 1
                #     = 2
                #
                # new even:
                #     previous ODD subarrays
                #
                #     = odd
                #     = 1

                odd, even = even + 1, odd

            # odd now tells us exactly:
            #
            # "How many odd-sum subarrays end
            #  at the current element?"
            #
            # Add those to the total.
            ans += odd

        return ans % MOD