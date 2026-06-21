"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None:None}

        old = head 
        #create a copy of the nodes
        while old:
            new =  Node(old.val)
            oldToNew[old] = new #map old to new node
            old = old.next 
        #restart from beginning
        old = head
        #connect the .next and .random pointers 
        while old:
            new = oldToNew[old] #copy new node from map
            new.next = oldToNew[old.next] 
            new.random = oldToNew[old.random] 
            old = old.next 
        return oldToNew[head]
        
        