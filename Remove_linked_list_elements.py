# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if(head == None):
            return head
        current = head
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next

            else:
                current = current.next

        return head

if __name__ == "__main__":
    s =  Solution()
    list = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))
    result = s.removeElements(list, 6)
    print(result)   
