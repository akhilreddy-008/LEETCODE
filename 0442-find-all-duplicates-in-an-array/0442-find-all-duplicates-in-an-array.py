class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''new=[]
        seen=set()
        for i in nums:
            if i in seen:
                new.append(i)
            else:
                seen.add(i)
        return new'''

        result=[]
        for num in nums:
            index=abs(num)-1
            if nums[index]<0:
                result.append(abs(num))
            else:
                nums[index]=-nums[index]
        return result