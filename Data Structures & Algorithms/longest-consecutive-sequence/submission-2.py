class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current = 0
        s = set()
        for n in nums:
            s.add(n)
        for n in s:
            count = 1
            if n-1 in s:
                continue
            for i in range(len(nums)):
                if n+1 in s:
                    count += 1
                    n+=1 
            if count > current:
                current = count 
        return current
                