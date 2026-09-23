class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        b=len(height)-1
        maxi=0
        while a<b:
            area=abs((a-b))*(min(height[a],height[b]))
            maxi=max(maxi,area)
            if height[a]<height[b]:
                a+=1
            else:
                b-=1
        return maxi