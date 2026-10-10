class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        n = len(strs)

        # For strings that are NOT cut, always use their
        # lexicographically largest orientation.
        best = [
            max(s, s[::-1])
            for s in strs
        ]

        ans = ""

        # Choose which string contains the cut.
        for i in range(n):

            # All the other strings occur intact and in their
            # original circular order.
            middle = (
                "".join(best[i + 1:]) +
                "".join(best[:i])
            )

            # The cut string is special:
            # we must consider BOTH orientations.
            for t in (strs[i], strs[i][::-1]):

                # Choose the character where the final string starts.
                for k in range(len(t)):

                    candidate = (
                        t[k:] +      # suffix of cut string
                        middle +     # all other strings
                        t[:k]        # prefix of cut string
                    )

                    ans = max(ans, candidate)

        return ans