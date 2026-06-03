class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)
        if target not in nums:
            return -1
            
        while start <= end: 
            middle = (end+start)//2
            if target < nums[middle]: #want to adjust to left half 
                end = middle
            elif target > nums[middle]: #adjust to right half
                start = middle 
            else: #target == nums[middle]
                return middle 
        return -1