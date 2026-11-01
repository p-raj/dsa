class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        total = 0
        score = 0

        for idx, cal in enumerate(calories):
            total += cal
            if idx >= k:
                total -= calories[idx - k]
            if idx >= k - 1:
                if total > upper:
                    score += 1
                if total < lower:
                    score -= 1
        return score
