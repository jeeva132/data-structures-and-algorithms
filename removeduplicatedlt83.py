# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res =set()

        temp = head
        prev = None
        while temp:
            if temp.val in res:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                res.add(temp.val)
                temp = temp.next
        return head
        
