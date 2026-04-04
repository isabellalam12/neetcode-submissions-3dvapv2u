class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a set because hashsets only contain unique elements 
        s = set()
        for i in nums:
            if i in s:
                return True
            else:   
                s.add(i)
        return False

        