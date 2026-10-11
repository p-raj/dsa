class Solution:
    def compress(self, chars: List[str]) -> int:
        len_ = len(chars)
        lft, rgt = 0, 0

        while rgt < len_:
            # this is the character we are going
            # to be processing
            chars[lft] = chars[rgt]
            # we will note its values in
            # the next position
            lft += 1
            nxt = rgt + 1
            while nxt < len_ and chars[nxt] == chars[rgt]:
                nxt += 1
            delta = nxt - rgt
            if delta > 1:
                for c in str(delta):
                    chars[lft] = c
                    lft += 1
            rgt = nxt
        return lft
