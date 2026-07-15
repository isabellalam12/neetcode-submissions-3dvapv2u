class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers = set()
        for n in nums: 
            if n in numbers:
                return n 
            numbers.add(n)
        return None

