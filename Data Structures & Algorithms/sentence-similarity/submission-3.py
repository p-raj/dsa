class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        map_ = {}
        for k, v in similarPairs:
            if k not in map_:
                map_[k] = set()
            if v not in map_:
                map_[v] = set()
            map_[k].add(v)
            map_[v].add(k)
        for k, v in zip(sentence1, sentence2):
            if (k == v) or (k in map_ and v in map_[k]) or (v in map_ and k in map_[v]):
                continue
            return False
        return True
        