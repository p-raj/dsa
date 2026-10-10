class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        to_ = nums2
        frm = nums1
        map_ = {}
        for idx, n in enumerate(to_):
            if n not in map_:
                map_[n] = list()
            map_[n].append(idx)
        res = []
        for n in frm:
            res.append(map_[n].pop())
        return res