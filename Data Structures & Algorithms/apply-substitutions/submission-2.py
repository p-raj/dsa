class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        text = text.split("%")
        R = {k:v for k,v in replacements if "%" not in v}
        D = {k:v for k,v in replacements if k not in R}
        for k, v in D.items():
            v = v.split("%")
            for idx, t in enumerate(v):
                if t in R:
                    v[idx] = R[t]
            R[k] = "".join(v)
        for idx, t in enumerate(text):
            if t in R:
                text[idx] = R[t]
        return "".join(text)
