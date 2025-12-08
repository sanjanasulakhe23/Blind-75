class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)   # step 1
        head.next.next = head                    # step 2
        head.next = None                         # step 3
        
        return new_head                          # step 4
