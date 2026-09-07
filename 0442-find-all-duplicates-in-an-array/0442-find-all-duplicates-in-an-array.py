class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        new=[]
        seen=set()
        for i in nums:
            if i in seen:
                new.append(i)
            else:
                seen.add(i)
        return new