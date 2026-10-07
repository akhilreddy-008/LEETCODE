class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = 0
        b = len(s1)
        count1 = {}
        for i in s1:
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1
        while b <= len(s2):
            new = s2[a:b]
            count2 = {}
            for i in new:
                if i in count2:
                    count2[i] += 1
                else:
                    count2[i] = 1
            if count1 == count2:
                return True
            a += 1
            b += 1
        return False