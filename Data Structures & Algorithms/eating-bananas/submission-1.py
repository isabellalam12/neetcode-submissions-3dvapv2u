class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input: number of piles, bananas per pile, and number of hours
        #output: k (bananas per hour)
        #constraint: can eat at most one pile per hour
        res = 0 
        l = 1
        r = max(piles)
        while l <= r:
            m = (l+r)//2
            hours = [-(x//-m) for x in piles]
            total_hours = sum(hours)
            if total_hours <= h:
                res = m
                r = m - 1
            else: 
                l = m + 1
        return res
        