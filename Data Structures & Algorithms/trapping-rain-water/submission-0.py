DBG = False
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        def next_max(lft: int, compare: int) -> int:
            nxt = lft + 1
            while nxt < len(height) and height[nxt] < compare:
                nxt += 1
            return nxt if nxt < len(height) else lft

        lft = 1
        while lft < len(height):
            base = height[lft]
            nxt_lft = next_max(lft, base)
            DBG and print(f"{lft=} -- {nxt_lft=} | {base=} {height[nxt_lft]=}")
            if lft == nxt_lft:
                lft += 1
            else:
                for i in range(lft + 1, nxt_lft + 1):
                    if height[i] < base:
                        res += base - height[i]
                    DBG and print(f"{res=} | {i=} | {base=} - {height[i]=}")
                lft = nxt_lft
        return res
