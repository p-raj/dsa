class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        N = {i:[] for i in range(10)}
        for num in nums:
            N[int(str(num)[0])].append(num)
        for key, arr in N.items():
            N[key] = sorted(arr, key=lambda x: x%10, reverse=True)
        
        res = ""
        for i in range(9, -1, -1):
            res += "".join(map(str, N[i]))
        if res[0] == "0":
            return "0"
        return res