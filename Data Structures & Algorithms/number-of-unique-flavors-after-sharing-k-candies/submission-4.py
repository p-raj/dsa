from collections import Counter

class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        C = candies

        # Initially give away C[0:k].
        # Count flavors in the kept candies.
        ccount = Counter(C[k:])
        uniq = len(ccount)
        answer = uniq

        for i in range(k, len(C)):
            # Leftmost candy of the old removed window
            # returns to the kept collection.
            w = C[i - k]

            if ccount[w] == 0:
                uniq += 1
            ccount[w] += 1

            # Rightmost candy of the new removed window
            # leaves the kept collection.
            l = C[i]

            ccount[l] -= 1
            if ccount[l] == 0:
                uniq -= 1

            answer = max(answer, uniq)

        return answer
