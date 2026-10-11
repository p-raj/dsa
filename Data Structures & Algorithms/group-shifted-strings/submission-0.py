class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        strings = sorted(strings, key= lambda x: len(x))
        groups = {}
        for s in strings:
            l = len(s)
            if l not in groups:
                groups[l] = list()
            groups[l].append(s)

        morphos = {}
        for l, gstrings in groups.items():
            if l == 1:
                morphos[0] = gstrings
            else:
                for gstring in gstrings:
                    diff = 0
                    idx = 0
                    while idx < l - 1:
                        d = abs(ord(gstring[idx])%12 - ord(gstring[idx+1])%12)
                        diff += (d * (10**(l-idx-2)))
                        idx += 1
                    if diff not in morphos:
                        morphos[diff] = list()
                    morphos[diff].append(gstring)
        return list(morphos.values())