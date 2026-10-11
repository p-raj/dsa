class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        map_ = {}
        for k, v in zip(sentence1, sentence2):
            map_[k] = v
        print(map_)
        for k, v in similarPairs:
            if (k not in map_) and (v not in map_):
                return False
            if (v in map_ and k != map_[v]) or (k in map_ and v != map_[k]):
                return False
        return True
