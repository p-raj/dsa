class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Voting Algorithm
        max_num1 = max_num2 = None
        cnt_num1 = cnt_num2 = 0

        for num in nums:
            if max_num1 == num:
                cnt_num1 += 1
            elif max_num2 == num:
                cnt_num2 += 1
            elif cnt_num1 == 0:
                max_num1 = num
                cnt_num1 = 1
            elif cnt_num2 == 0:
                max_num2 = num
                cnt_num2 = 1
            else:
                cnt_num1 -= 1
                cnt_num2 -= 1
        print(max_num1, max_num2, cnt_num1, cnt_num2)
        cnt_num1 = cnt_num2 = 0
        for num in nums:
            if num == max_num1:
                cnt_num1 += 1
            elif num == max_num2:
                cnt_num2 += 1
        third = math.floor(len(nums)/3)
        res = []
        if cnt_num1 > third:
            res.append(max_num1)
        if cnt_num2 > third:
            res.append(max_num2)
        return res