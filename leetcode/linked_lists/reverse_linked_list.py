# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        root = ListNode(values.pop())
        current = root
        for i in range(len(values) - 1 , -1, -1):
            current.next = ListNode(values[i])
            current = current.next
        return root

def print_linked_list(head):
    current = head
    s = ""
    while current:
        s += f"{current.val} - "
        current = current.next
    print(s)

if __name__ == "__main__":
    # [1,2,3,4,5]
    # [1,2]
    f = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print_linked_list(Solution().reverseList(f)) # 5 - 4 - 3 - 2 - 1 - 
    f = ListNode(1, ListNode(2, None))
    print_linked_list(Solution().reverseList(f)) # 2 - 1 - 
    print_linked_list(Solution().reverseList(None)) # 
            

