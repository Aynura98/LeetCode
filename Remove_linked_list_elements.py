# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def asList(self):
        current = self
        list = []
        while current != None:
            list.append(current.val)
            current = current.next
        return list
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        current = dummy_head

        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next

            else:
                current = current.next

        return dummy_head.next

if __name__ == "__main__":
    s =  Solution()
    given_list = ListNode(1, ListNode(2,  ListNode(7, ListNode(5, None))))
    result = s.removeElements(given_list, 7)
    if(result == None):
        print("[]")
    else:
        print(result.asList())
    print(result)   
