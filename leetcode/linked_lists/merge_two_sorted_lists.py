from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        aux1 = list1
        aux2 = list2
        new_head = ListNode(None)
        temp = new_head
        while aux1 and aux2:
            if aux1.val <= aux2.val:
                temp.next = aux1
                aux1 = aux1.next
            elif aux2.val <= aux1.val:
                temp.next = aux2
                aux2 = aux2.next
            temp = temp.next
        if aux2:
            temp.next = aux2
        elif aux1:
            temp.next = aux1

        return new_head.next
    
def print_linked_list(head):
    current = head
    s = ""
    while current:
        s += f"{current.val} - "
        current = current.next
    print(s)

if __name__ == "__main__":
    # 1 - 1 - 2 - 3 - 4 - 4 - 
    #
    # 0 - 
    f = ListNode(1, ListNode(2, ListNode(4, None)))
    s = ListNode(1, ListNode(3, ListNode(4, None)))
    print_linked_list(Solution().mergeTwoLists(f, s)) # 5 - 4 - 3 - 2 - 1 - 
    print_linked_list(Solution().mergeTwoLists(None, None)) # 2 - 1 - 
    s = ListNode(0)
    print_linked_list(Solution().mergeTwoLists(None, s)) # 
        