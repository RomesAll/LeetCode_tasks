# Definition for singly-linked list.
class Node:
    def __init__(self, *args):
        self.start = None
        current = None

        for i in range(len(args)):
            if i == 0:
                self.start = ListNode(args[i])
                current = self.start
                continue
            
            current.next = ListNode(args[i])
            current = current.next
            
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass



l1 = Node(2,4,3)
l2 = Node(5,6,4)

s = Solution(l1, l2)

