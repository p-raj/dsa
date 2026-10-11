class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        text = text.split("%")
        R = {k:v for k,v in replacements}
        for idx, t in enumerate(text):
            if t in R:
                text[idx] = R[t]
        return "".join(text)
