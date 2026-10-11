class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        num_strs = f"{len(strs):08X}"
        for sidx_, str_ in enumerate(strs):
            for cidx_, char_ in enumerate(str_):
                encoded += f"{sidx_:08X}{cidx_:08X}{ord(char_):08X}"
        return num_strs+encoded

    def decode(self, s: str) -> List[str]:
        cursor = 0
        num_strs = int(s[cursor:cursor+8])
        cursor += 8
        strs = [""] * num_strs
        while cursor < len(s):
            sidx_ = int(s[cursor:cursor+8], 16)
            cidx_ = int(s[cursor+8:cursor+16], 16)
            char_ = chr(int(s[cursor+16:cursor+24], 16))
            cursor += 24
            strs[sidx_] += char_
        return strs