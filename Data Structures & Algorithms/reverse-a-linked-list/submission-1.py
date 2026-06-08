# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #input: head node of a list (singly linked list)
            # 1 --> 2 --> 3
        #output: head node of reversed list 
            # 1 <-- 2 <-- 3 
        #edge case: empty list
        pre = None
        post = head 

        while post: 
            temp = post.next
            post.next = pre 

            pre = post 
            post = temp 

        return pre


