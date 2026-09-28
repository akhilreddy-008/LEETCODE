class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        a=0
        b=len(people)-1
        new=0
        while a<=b:
            if people[a]+people[b]<=limit:
                a+=1
                b-=1
            else:
                b-=1
            new+=1
        return new