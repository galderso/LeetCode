class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous