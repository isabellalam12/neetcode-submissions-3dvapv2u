class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0 
        r = len(nums)-1
        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: #m points to the greater increasing portion of the list
                #search the right portion of the list 
                l = m + 1
            else: #m points to the lesser increasing portion of the list
                #search the left portion of the list 
                r = m - 1
        return res
