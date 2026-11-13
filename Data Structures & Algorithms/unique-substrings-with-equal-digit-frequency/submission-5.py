class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        # Approach: LCP
        suffixes = [s[i:] for i in range(len(s))]
        suffixes.sort()
        # lexicographical order
        # for suffixes -
        # a
        # an
        # ana
        # anan
        # anana
        # "[an]ana" is a suffix of the original string "b{anana}".
        # "[an]" is a prefix of that suffix.
        # Therefore, "[an]" is a substring of the original string.
        # 💡 Every substring can be represented as a prefix of some suffix.
        # All strings sharing a fixed prefix occupy one contiguous interval in lexicographic order.
        # Now suppose the current suffix is "anana".
        # If some earlier suffix shared "ana" with it, all the suffixes beginning with "ana" would be grouped together.
        # Therefore, the immediately previous suffix must also begin with "ana".
        # thats why we need to keep track of the prev
        prev = ""
        # LCP of suffix with prev
        # makes sure that we have processed
        # the substrings where suffix
        answer = 0
        for sfx in suffixes:
            overlap = 0
            while overlap < min(len(prev), len(sfx)) and prev[overlap] == sfx[overlap]:
                overlap += 1
                # The LCP is the longest prefix of the current suffix
                # that has already appeared in an earlier suffix.
                # Prefixes of length <= overlap are duplicates.
                # Longer prefixes represent new substring values.

            freq = [0] * 10

            for length, ch in enumerate(sfx, 1):
                digit = int(ch)
                freq[digit] += 1

                # freq now describes sfx[:length].
                if length > overlap:
                    # This substring is new.
                    # are all the freq
                    # counter equal
                    # we have an answer
                    if len(set([f for f in freq if f])) == 1:
                        answer += 1

            prev = sfx
        return answer
