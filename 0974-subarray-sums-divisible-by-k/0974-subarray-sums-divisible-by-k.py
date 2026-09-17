class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = 0
        s = 0
        d = {0: 1}
        for i in nums:
            s += i
            r = s % k
            if r in d:
                cnt += d[r]
            d[r] = d.get(r, 0) + 1
        return cnt