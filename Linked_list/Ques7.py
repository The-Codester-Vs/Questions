# Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.


class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Solution(object):
   def getIntersectionNode(self, headA, headB):
      """
      :type head1, head1: ListNode
      :rtype: ListNode
      """
      dict = {}
      while headA:
         dict[headA]=1
         headA = headA.next
      while headB:
         if headB in dict:
            return headB
         headB = headB.next
      return None
  
headA = ListNode(4)
headB = ListNode(5)
Intersect =  ListNode(4, ListNode(5))
headA.next = ListNode(1, Intersect)
headB.next = ListNode(0, ListNode(1, Intersect))
ob1 = Solution()
op = ob1.getIntersectionNode(headA, headB)
print("Intersection:",op.data)