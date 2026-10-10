class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        A = set(allowed)
        W = [set(w) for w in words]
        count = 0
        for w in W:
            if w.issubset(A):
                count += 1
        return count