class Solution:
    def moveZeroes(self, nums: List[int]) -> None:   
        a=0
        for b in range(len(nums)):
            if nums[b]!=0:
                nums[a],nums[b]=nums[b],nums[a]
                a+=1
        return nums