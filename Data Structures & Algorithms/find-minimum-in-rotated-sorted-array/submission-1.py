class Solution:
    def findMin(self, nums: List[int]) -> int:
        #re-sort the list
        l = 0 
        r = len(nums)-1 
        res = 0 
        while nums[l] > nums[r] and l<r:
            nums.append(nums[res])
            l += 1
            res += 1
        
        #binary search for smallest
        return nums[res]