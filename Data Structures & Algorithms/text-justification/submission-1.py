class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # greedy is the only correct solution
        # for greedy we pack as many words as possible
        # in the line
        # word space*? word space*?
        # word space*? word space*?

        
        # DP is an incorrect solution here
        n = len(words)
        memo = {}
        soln = {}

        def fn(i: int) -> int:
            """
            Minimum number of lines required
            to place words[i:].
            """

            if i == n:
                return 0

            if i in memo:
                return memo[i]

            best = float("inf")

            # Width of words[i:j+1], including
            # the mandatory one space between words.
            width = 0

            for j in range(i, n):
                if j == i:
                    # First word on line: no leading space.
                    width = len(words[j])
                else:
                    # Every additional word requires
                    # at least one separator.
                    width += 1 + len(words[j])

                if width > maxWidth:
                    break

                # Current line contains words[i:j+1].
                candidate = 1 + fn(j + 1)
                if (
                    candidate < best
                    or
                    (candidate == best and j > soln.get(i, -1))
                ):
                    best = candidate
                    soln[i] = j

            memo[i] = best
            return best

        lines_needed = fn(0)

        print("minimum lines:", lines_needed)
        lines = []
        i = 0

        def justify(line_words, maxWidth, is_last):
            # Last line: exactly one space between words,
            # remainder goes at the end.
            if is_last:
                line = " ".join(line_words)
                return line + " " * (maxWidth - len(line))

            # A line containing one word has no internal gaps.
            if len(line_words) == 1:
                word = line_words[0]
                return word + " " * (maxWidth - len(word))

            word_chars = sum(len(word) for word in line_words)

            total_spaces = maxWidth - word_chars
            gaps = len(line_words) - 1

            base_spaces = total_spaces // gaps
            extra_spaces = total_spaces % gaps

            line = ""

            for k in range(gaps):
                line += line_words[k]

                # Leftmost `extra_spaces` gaps get one extra space.
                spaces_here = base_spaces
                if k < extra_spaces:
                    spaces_here += 1

                line += " " * spaces_here

            line += line_words[-1]

            return line

        result = []
        while i < len(words):
            j = soln[i]

            line_words = words[i : j + 1]

            is_last = j == len(words) - 1

            result.append(justify(line_words, maxWidth, is_last))

            i = j + 1
        return result
        ##################
        # INCORRECT DP
        # W_SPACE = " "
        # L_SPACE = 1
        # pack as many words in each line as possible =>
        # => minimize the number of lines used
        # sequence of words has to be maintained
        # assuming words till i have been packed well
        # the i+1th word either goes on line j or on a new line j+1
        # if the i+1th goes in the same line j, there are two choices
        # pad left with space, or use the word
        # all lines are of equal width = maxWidth
        # once the words are packed, reformat the last line
        # f(i, width)
        # if maxWidth < (width + len(word[i]))
        # two choices > len(word[i]), or len(" ")
        # based on choices the i+1, and (width-l_word) or (width-l_space)
        # else the only choice is to use the word (i+1, width)
        # based on this, how to minimize the lines?
        # f(n,?) = 0
        # f(0,0) = 0
        # f(?, maxWidth) = 1
        # memo = {}
        # soln = {}

        # def fn(idx: int, wdth: int) -> int:
        #     ky = (idx, wdth)
        #     if ky in memo:
        #         return memo[ky]
        #     if idx == len(words):
        #         return 0
        #     word = words[idx]
        #     l_word = len(word)
        #     if wdth == 0:
        #         # use the word
        #         memo[ky] = fn(idx+1, l_word)
        #     elif maxWidth < (l_word + wdth):
        #         memo[ky] = fn(idx+1, l_word) + 1  # next line
        #     else:
        #         memo[ky] = min(
        #             # use space
        #             fn(idx, wdth + L_SPACE),
        #             # use word
        #             fn(idx + 1, wdth + l_word),
        #         )
        #     return memo[ky]

        # print(fn(0, 0))
        # return []
