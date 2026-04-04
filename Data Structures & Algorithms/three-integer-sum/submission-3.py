class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #enumerate turns the list into an ordered pair (index, value)
        #loop goes thru, using each value in nums as beginning number
        for i, a in enumerate(nums):
            #not the 1st element (so we dont access invalid previous index)
            #AND same value as before --> skip 
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1 
                else:
                    res.append([a,nums[l],nums[r]])
                #[-2,-2,0,0,2,2] 
                # left is farthest left -2 and right is farthest right 2
                # only need to update 1 --> above statements will update the 
                # other pointer as needed
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res