from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        CC = Counter(chars)
        WC = [Counter(w) for w in words]
        count = 0
        for idx, wc in enumerate(WC):
            can_form = True
            for k,v in wc.items():
                if k not in CC or (k in CC and v > CC[k]):
                    can_form = False
                    break
            if can_form:
                count += len(words[idx])
        return count
