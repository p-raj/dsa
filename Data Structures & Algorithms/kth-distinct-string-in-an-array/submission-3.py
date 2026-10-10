class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        H = {}
        for c in arr:
            if c not in H:
                H[c] = 0
            H[c] += 1
        
        # h = [k for k,v in H.items() if v == 1]
        # return "" if k > len(h) else h[k-1]
        for c in arr:
            if H[c] == 1:
                k-=1
                if k == 0:
                    return c
        return ""