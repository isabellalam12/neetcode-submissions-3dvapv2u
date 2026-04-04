class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        for i in range(len(nums)):
            d = target-nums[i]
            if d in h and h[d] != i:
                return [i,h[d]]
        return []
    
                
