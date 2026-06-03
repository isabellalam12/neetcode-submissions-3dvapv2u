class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)-1
        while start <= end: 
            middle = (end+start)//2
            if target < nums[middle]: #want to adjust to left half 
                end = middle-1
            elif target > nums[middle]: #adjust to right half
                start = middle +1
            else: #target == nums[middle]
                return middle 
        return -1