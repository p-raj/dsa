class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        map_ = {}
        for k, v in similarPairs:
            map_[k] = v
            map_[v] = k
        for k, v in zip(sentence1, sentence2):
            if (k in map_ and map_[k] == v) or (v in map_ and map_[v] == k) or (not map_ and k == v):
                continue
            return False
        return True
        