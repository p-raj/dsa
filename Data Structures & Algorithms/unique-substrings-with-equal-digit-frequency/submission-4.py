class TriNode:
    def __init__(self):
        self.children = dict()


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        # approach 2: trie
        root = TriNode()
        answer = 0

        for lft in range(len(s)):
            current = root
            freq = [0] * 10
            for rgt in range(lft, len(s)):
                is_new_node = False
                digit = int(s[rgt])
                freq[digit] += 1
                
                if digit not in current.children:
                    current.children[digit] = TriNode()
                    is_new_node = True

                current = current.children[digit]
                if is_new_node and len(set([i for i in freq if i > 0])) == 1:
                    answer += 1

        return answer
