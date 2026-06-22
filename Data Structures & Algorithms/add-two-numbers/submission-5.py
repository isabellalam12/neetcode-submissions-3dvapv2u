# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode(None, None)
        head = sum
        carry = 0
        #iterate through each node (edge case: one number is longer than the other --> handle null)
        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
        
            temp = val1 + val2 + carry
            carry = temp // 10 
            digit = temp % 10 
                
            sum.next = ListNode(digit) 
            sum = sum.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
            #add the numbers 
                #if >=10, then carry the one
        return head.next
        
        #return reversed sum list