class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       h = {}
       for i in range(len(nums)):
            number = target - nums[i]
            if number in h:
                return [h.get(number), i]
            h[nums[i]] = i 
         
        




    
                
