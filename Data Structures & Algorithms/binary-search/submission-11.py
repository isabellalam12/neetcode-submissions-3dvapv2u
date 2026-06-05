class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input: list of distinct, ascending integers and target integer
        #output: index or -1 
        #edge cases: target not in list, empty list, non-integer list

        l = 0 
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] < target: 
                l = m + 1
            elif nums[m] > target: 
                r = m - 1
            else: 
                return m 
        return -1
