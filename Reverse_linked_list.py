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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node

        return new_list





if __name__ == "__main__":
    s =  Solution()
    given_list = ListNode(1, ListNode(2,  ListNode(3, ListNode(4, ListNode(5, None)))))
    result = s.reverseList(given_list)
    if(result == None):
        print("[]")
    else:
        print(result.asList())
    print(result)   
    