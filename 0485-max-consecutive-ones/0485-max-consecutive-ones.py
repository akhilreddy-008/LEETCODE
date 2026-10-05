class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        '''cnt=0
        max_cnt=0
        for i in nums:
            if i ==  :
                cnt+=1
            else:
                cnt=0
            if max_cnt<cnt:
                max_cnt=cnt
        return max_cnt'''
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i]!=0:
                prefix[i] = prefix[i-1] + nums[i]
            else:
                prefix[i]=0
        return max(prefix)