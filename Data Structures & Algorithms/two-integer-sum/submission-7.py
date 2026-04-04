class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            d = target-nums[i] 
            if d in h and h[d] != i:
                return [h[d],i]
            else:
                h[nums[i]] = i
        return []
    
                
