class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        if abs(ns - nt) > 1:
            return False

        i = j = 0

        # Match common prefix
        while i < ns and j < nt and s[i] == t[j]:
            i += 1
            j += 1

        # No mismatch occurred.
        # Exactly one edit is possible only if one string
        # has exactly one remaining character.
        if i == ns or j == nt:
            return (ns - i) + (nt - j) == 1

        # First mismatch consumes our one allowed edit.
        if ns == nt:
            # replacement
            i += 1
            j += 1

        elif ns < nt:
            # insert into s
            j += 1

        else:
            # delete from s
            i += 1

        # No more edits are allowed.
        while i < ns and j < nt:
            if s[i] != t[j]:
                return False
            i += 1
            j += 1

        return i == ns and j == nt