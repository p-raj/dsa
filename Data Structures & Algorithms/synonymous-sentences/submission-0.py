import itertools
from dataclasses import dataclass


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        vertex = dict()
        hmap = dict()
        dsets = []
        for w, s in synonyms:
            if w not in vertex:
                nw = Node(w)
                make_set(nw)
                vertex[w] = nw
            if s not in vertex:
                ns = Node(s)
                make_set(ns)
                vertex[s] = ns
            dsets.append([vertex[w], vertex[s]])
        for w, s in dsets:
            union_set(w, s)
        for w, s in dsets:
            par = find_set(w).data
            if par not in hmap:
                hmap[par] = set()
            hmap[par].add(w.data)
            hmap[par].add(s.data)
        # print(hmap, vertex)
        text_tokens = text.split(" ")
        replacement_idx_map = {}
        replacement_word_map = {}
        for idx, txt in enumerate(text_tokens):
            if txt in vertex:
                words = sorted(list(hmap[find_set(vertex[txt]).data]))
                replacement_idx_map[idx] = words
                for w in words:
                    replacement_word_map[w] = idx
        lists = replacement_idx_map.values()
        combinations = list(itertools.product(*lists))
        # print(combinations, replacement_word_map)
        res = []
        for combos in combinations:
            for w in combos:
                idx = replacement_word_map[w]
                text_tokens[idx] = w
            res.append(" ".join(text_tokens))
        return res
        


@dataclass
class Node:
    data: str
    rank: int = 0
    parent: Node | None = None

    def __str__(self):
        return f"<Node: {self.data=} {self.rank=} {self.parent=}/>"
    
    def __hash__(self):
        return self.data


def make_set(x: Node) -> None:
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    x.parent = x


def union_set(x: Node, y: Node) -> None:
    x, y = find_set(x), find_set(y)
    if x == y:
        return

    elif x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def find_set(x: Node) -> Node:
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent
