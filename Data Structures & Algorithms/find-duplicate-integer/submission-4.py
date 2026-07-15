class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0 
        while slow == 0 or slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow2 = 0 
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
        



        
'''
[1,2,3,2,2]
[1,2,3,4,5,6,6]
[3,2,1,4,4]
[1,1]
[4,1,2,3,4]
[3,2,4,1,4]

[0,1,2,3,4]
[4,3,2,1,1]
'''