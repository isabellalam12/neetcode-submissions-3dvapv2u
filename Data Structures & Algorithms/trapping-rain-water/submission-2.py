class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        l = 0 
        r = len(height) - 1
        #set equal to height[l] and height[r] in case 
        #those heights are the max
        maxL= height[l]
        maxR = height[r]
        res = 0
        while l < r:
            if height[l]< height[r]:
                l+=1
                #this ordering ensures that no negatives are added to res
                maxL = max(maxL, height[l])
                #add max() so either 0 or positive number added
                res += max(0,(min(maxL,maxR)-height[l]))
            else:
                r-=1
                maxR = max(maxR, height[r])
                res += max(0,(min(maxL,maxR)-height[r]))
        return res

