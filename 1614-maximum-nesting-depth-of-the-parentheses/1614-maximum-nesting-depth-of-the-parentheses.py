class Solution:
    def maxDepth(self, s: str) -> int:
        l = 0
        r = 0
        for i in s:
            if i == "(":
                l += 1
                if l > r:
                    r = l
            elif i == ")":
                l -= 1
        return r