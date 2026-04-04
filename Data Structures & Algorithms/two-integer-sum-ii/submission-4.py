class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #idea: starting with a pointer at the far right --> -- r when larger 
        # and/or equal to target; else, ++ l 
        r = len(numbers) - 1
        l = 0 
        while l < r:
            if  numbers[l] + numbers[r] < target:
                l = l + 1
            elif numbers[l] + numbers[r] > target:
                r = r - 1 
            else:
                return [l+1,r+1]
            
            