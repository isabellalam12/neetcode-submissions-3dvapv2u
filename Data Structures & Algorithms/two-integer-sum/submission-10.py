class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       h = {}
       i = 0
       for number in nums:
            find = target - number
            if find in h:
                return [h.get(find,0), i]
            h[number] = i
            i= i+1
        




    
                
