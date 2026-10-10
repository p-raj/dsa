class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        text = text.split("%")
        R = {k: v for k, v in replacements if "%" not in v}
        D = {k: v for k, v in replacements if "%" in v}
        graph = []
        to_del = []
        while len(D):
            while to_del:
                del D[to_del.pop()]
            for k,v in D.items():
                v = v.split("%")
                for i, c in enumerate(v):
                    if c in D:
                        graph.append((k, D[c]))
                        v[i] = f'%{c}%'
                    if c in R:
                        v[i] = R[c]
                s = "".join(v)
                if '%' in s:
                    D[k] = s
                else:
                    to_del.append(k)
                    R[k] = s
        for idx, t in enumerate(text):
            if t in R:
                text[idx] = R[t]
        return "".join(text)