import itertools
from dataclasses import dataclass
from collections import defaultdict
from typing import List


@dataclass(eq=False)
class Node:
    data: str
    rank: int = 0
    parent: Node | None = None


def make_set(x: Node) -> None:
    x.rank = 0
    x.parent = x


def find_set(x: Node) -> Node:
    # Path compression
    if x is not x.parent:
        x.parent = find_set(x.parent)

    return x.parent


def union_set(x: Node, y: Node) -> None:
    x = find_set(x)
    y = find_set(y)

    # Already in the same component
    if x is y:
        return

    # Union by rank
    if x.rank > y.rank:
        y.parent = x

    elif x.rank < y.rank:
        x.parent = y

    else:
        # Same rank: either one may become the root.
        x.parent = y
        y.rank += 1


class Solution:
    def generateSentences(
        self,
        synonyms: List[List[str]],
        text: str
    ) -> List[str]:

        nodes = {}

        # --------------------------------------------------
        # 1. Construct synonym equivalence classes.
        # --------------------------------------------------

        for a, b in synonyms:

            if a not in nodes:
                nodes[a] = Node(a)
                make_set(nodes[a])

            if b not in nodes:
                nodes[b] = Node(b)
                make_set(nodes[b])

            union_set(nodes[a], nodes[b])

        # --------------------------------------------------
        # 2. root -> all words in that equivalence class
        # --------------------------------------------------

        groups = defaultdict(list)

        for word, node in nodes.items():
            root = find_set(node)
            groups[root.data].append(word)

        # Sorting each component is important because we
        # eventually want lexicographic output.
        for words in groups.values():
            words.sort()

        # --------------------------------------------------
        # 3. Determine possible words for each text position.
        # --------------------------------------------------

        tokens = text.split()

        choices = []

        for word in tokens:

            if word in nodes:
                root = find_set(nodes[word])
                choices.append(groups[root.data])

            else:
                # Non-synonym word has exactly one possibility:
                # itself.
                choices.append([word])

        # --------------------------------------------------
        # 4. Cartesian product generates every sentence.
        # --------------------------------------------------

        result = []

        for combination in itertools.product(*choices):
            result.append(" ".join(combination))

        return result