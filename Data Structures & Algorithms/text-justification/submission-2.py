class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # greedy is the faster correct solution than DP
        # for greedy we pack as many words as possible
        # in the line
        # word space*? word space*?
        # word space*? word space*?
        # For the current line, keep taking the next word while it still
        # fits using the minimum required one-space separators.
        def packing(words, maxWidth):
            lines = []
            idx = 0
            while idx < len(words):
                nxt = idx
                width = len(words[idx])
                while ((nxt + 1) < len(words)) and (width + 1 + len(words[nxt + 1])) <= maxWidth:
                    nxt += 1
                    width += (1 + len(words[nxt]))
                
                lines.append(
                    words[idx: nxt+1]
                )
                idx = nxt + 1
            return lines
        
        
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

        lines = packing(words, maxWidth)
        result = []
        for idx, line in enumerate(lines):
            result.append(justify(
                line,
                maxWidth,
                idx == len(lines)-1
            ))
        return result
