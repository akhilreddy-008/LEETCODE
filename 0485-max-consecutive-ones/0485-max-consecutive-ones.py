class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cnt=0
        max_cnt=0
        for i in nums:
            if i ==  1:
                cnt+=1
            else:
                cnt=0
            if max_cnt<cnt:
                max_cnt=cnt
        return max_cnt