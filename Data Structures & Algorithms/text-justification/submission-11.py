class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            # Find the maximum number of words that fit.
            j = i + 1
            letters = len(words[i])

            while (
                j < n
                and letters + (j - i) + len(words[j]) <= maxWidth
            ):
                letters += len(words[j])
                j += 1

            # words[i:j] belong to this line.
            gaps = j - i - 1
            is_last = (j == n)

            # Last line or single-word line:
            # left justify with one space between words.
            if is_last or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                total_spaces = maxWidth - letters

                base = total_spaces // gaps
                extra = total_spaces % gaps

                parts = []

                for k in range(i, j - 1):
                    parts.append(words[k])

                    spaces = base
                    if k - i < extra:
                        spaces += 1

                    parts.append(" " * spaces)

                parts.append(words[j - 1])

                line = "".join(parts)

            result.append(line)
            i = j

        return result