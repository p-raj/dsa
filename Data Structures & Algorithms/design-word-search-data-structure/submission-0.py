class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]

        while stack:
            node, i = stack.pop()

            if i == len(word):
                if node.word:
                    return True
                continue

            ch = word[i]

            if ch == ".":
                for child in node.children.values():
                    stack.append((child, i + 1))
            else:
                if ch in node.children:
                    stack.append((node.children[ch], i + 1))

        return False
