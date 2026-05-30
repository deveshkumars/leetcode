# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def nodeify(self, lst) -> ListNode:
        first = lst.pop()
        if len(lst) == 0:
            returnobj = ListNode(first)
        else:
            returnobj = ListNode(first, self.nodeify(lst))
        return returnobj


    def listSum(self, lst, order=0):
        val = lst.val * (10 ** order)
        if not lst.next:
            return val
        else:
            return val + self.listSum(lst.next, order+1)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # return self.nodeify([1,2,3])
        return self.nodeify(list(map(int, str(self.listSum(l1) + self.listSum(l2)))))
