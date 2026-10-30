class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        C = candies
        ccount = [0] * 100001
        uniq = 0
        # assuming removal for first K elements
        for i in range(k, len(C)):
            c = C[i]
            if ccount[c] == 0:
                uniq += 1
            ccount[c] += 1

        answer = uniq

        # now we start moving the window
        for i in range(k, len(C)):
            # the element we keep
            w = candies[i - k]
            if ccount[w] == 0:
                uniq += 1
            ccount[w] += 1
            # the element we loose
            l = candies[i]
            ccount[l] -= 1
            if ccount[l] == 0:
                uniq -= 1

            answer = max(answer, uniq)

        return answer
