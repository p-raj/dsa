DBG = False
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        # spend: choose token + spend power, score += 1, power -= token
        # gain: choose token + spend score, score -= 1, power += token
        # goal:maximize the score
        # approach: greedy
        # spend minimum tokens to gain score
        # spend maximum tokens to gain power
        
        imint = 0
        imaxt = len(tokens) - 1
        smax = 0
        while imaxt >= imint:
            DBG and print(f"{power=}, {score=}")
            if power - tokens[imint] >= 0:
                power -= tokens[imint]
                score += 1
                imint += 1
            elif score > 0:
                power += tokens[imaxt]
                score -= 1
                imaxt -= 1
            else:
                return smax
            if smax < score:
                smax = score
            DBG and print(f"{power=}, {score=}, {smax=}, {imint=}, {imaxt=}")
        return smax
            