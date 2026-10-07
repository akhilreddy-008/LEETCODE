class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=0
        b=len(s1)
        while b<=len(s2):
            new=s2[a:b]
            if sorted(s1)==sorted(new):
                return True
            a+=1
            b+=1
        return False