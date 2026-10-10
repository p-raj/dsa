class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resp = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in resp:
                resp[ss] = list()
            resp[ss].append(s)
        return list(resp.values())