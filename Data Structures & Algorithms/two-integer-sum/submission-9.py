class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number not in h:
                h[nums[i]] = i
            else: 
                return [h.get(number,0),i]


    
                
