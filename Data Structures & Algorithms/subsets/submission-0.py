from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        soln = []
        # any ak would be extracted out of Sk
        # Sk is just {true or false}
        # so, ak would be just true or false
        def is_a_soln(partial_soln_vec, move_counter_k, input_data):
            k = move_counter_k
            data = input_data
            return k == len(data) - 1

        def process_soln(partial_soln_vec, move_counter_k, input_data):
            a = partial_soln_vec
            data = input_data
            soln.append([data[idx] for idx, val in enumerate(a) if val is True])

        # possible candidates for the kth position of a,
        # given the contents of the first k−1 positions
        def construct_candidates(partial_soln_vec, move_counter_k, input_data):
            return (True, False)

        def move(partial_soln_vec, move_counter_k, input_data):
            pass
        
        def undo(partial_soln_vec, move_counter_k, input_data):
            pass

        def bt(partial_soln_vec, move_counter_k, input_data):
            a = partial_soln_vec
            k = move_counter_k
            data = input_data
            # print(a, k, data)
            if is_a_soln(a, k, data):
                process_soln(a, k, data)
            else:
                k += 1
                if k >= len(input_data):
                    return
                for c in construct_candidates(a, k, data):
                    a[k] = c
                    move(a, k, data)
                    bt(a, k, data)
                    undo(a, k, data)

        bt([None] * len(nums), -1, nums)
        return soln

# Solution().subsets([1,2,3])