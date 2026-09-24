class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        out = -1
        for j in range(len(nums)):
            i = nums[j]
            a = 0
            while i != 0:
                a += i % 10
                i = i // 10
            if a == j:
                out = j
                break
        return out