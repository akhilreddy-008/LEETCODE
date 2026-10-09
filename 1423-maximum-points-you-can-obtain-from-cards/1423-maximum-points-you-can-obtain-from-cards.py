class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        res = sum(cardPoints[:k])
        maxi = res
        for i in range(k):
            res -= cardPoints[k - 1 - i]
            res += cardPoints[len(cardPoints) - 1 - i]
            maxi = max(maxi, res)
        return maxi