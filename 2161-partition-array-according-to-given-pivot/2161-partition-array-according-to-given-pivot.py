class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        new=[]
        for i in nums:
            if i<pivot:
                new.append(i)
        for i in nums:
            if i==pivot:
                new.append(i)
        for i in nums:
            if i>pivot:
                new.append(i)
        return new