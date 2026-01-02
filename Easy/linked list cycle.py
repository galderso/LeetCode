class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        found = set()
        while head:

            if head in found:
                return True
            else:
                found.add(head)
                head = head.next
        return False