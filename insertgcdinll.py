import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy = head
        fast = dummy
        slow = dummy
        # def gcd(a,b):

        #     while b:
        #         a = b
        #         b = a%b
        #     return a
        while fast and fast.next:
            fast = fast.next
            newnode = ListNode(val=math.gcd(slow.val,fast.val),next=fast)
            slow.next = newnode
            slow = slow.next.next
        
        return dummy
