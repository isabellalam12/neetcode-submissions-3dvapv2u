class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #idea: starting with a pointer at the far right --> -- when larger 
        # and/or equal to target 
        r = len(numbers) - 1
        l = 0 
        while l < r:
            if  l < r and numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            if numbers[l] + numbers[r] > target:
                r = r - 1 
            else:
                l = l + 1
            
            