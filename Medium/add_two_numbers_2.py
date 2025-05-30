# Definition for singly-linked list.
class Node:
    def __init__(self, *args):
        self.start = None
        self.len = len(args)

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
         self.remainder = 0


class Solution:
    
    def check(self, max_l, other_l=None):

        stage = []

        if other_l:
            sum_item_list = max_l.val + other_l.val + max_l.remainder
        else:
            sum_item_list = max_l.val + max_l.remainder

        stage.append(sum_item_list % 10)

        if sum_item_list > 9:
            if max_l.next is not None:
                max_l.next.remainder = 1
            else:
                stage.append(1)
        
        return stage

    def addTwoNumbers(self, n1:Node, n2:Node) -> ListNode:
        
        result_list = []

        max_l = n1.start if n1.len >= n2.len else n2.start
        other_l = n2.start if max_l == n1.start else n1.start



        while max_l != None:
            
            if other_l:
                result_list += self.check(max_l, other_l)
            else:
                result_list += self.check(max_l)

            max_l = max_l.next
            if other_l:
                other_l = other_l.next

        return result_list
        



l1 = Node(2,4,3)
l2 = Node(5,6,4)

s = Solution()
res = s.addTwoNumbers(l1, l2)
print(res)
