class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1_chr = sentence1.split(" ")
        s2_chr = sentence2.split(" ")

        sl_chr = s2_chr if len(s2_chr) > len(s1_chr) else s1_chr
        ss_chr = s2_chr if len(s2_chr) <= len(s1_chr) else s1_chr

        lft_sl = 0
        lft_ss = 0
        budget = 1
        while lft_sl < len(sl_chr) and lft_ss < len(ss_chr) and budget:
            if sl_chr[lft_sl] == ss_chr[lft_ss]:
                lft_sl += 1
                lft_ss+= 1
            else:
                # now we have to keep expanding window
                # till the pinned word matches
                # we can fill in those words
                pinned = ss_chr[lft_ss]
                while lft_sl < len(sl_chr) and sl_chr[lft_sl] != pinned:
                    lft_sl += 1
                budget -= 1

        while lft_sl < len(sl_chr) and lft_ss < len(ss_chr):
            if sl_chr[lft_sl] == ss_chr[lft_ss]:
                lft_sl += 1
                lft_ss+= 1
            else:
                return False
        
        return lft_sl == len(sl_chr) and lft_ss == len(ss_chr)