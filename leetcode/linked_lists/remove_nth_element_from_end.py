# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        counter = 0
        nodes = {}
        while current:
            nodes[counter] = current
            counter += 1
            current = current.next

        target_index = len(nodes) - n - 1
        prev_node = nodes.get(target_index, None)
        if prev_node:
            prev_node.next = prev_node.next.next
        elif nodes[0].next is not None:
            head = nodes[0].next
        else:
            head = None

        return head
    
def linked_list_from_array(elements):
    head = ListNode(elements.pop(0))
    current = head
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    s = ""
    while current:
        s += f"{current.val} - "
        current = current.next
    print(s)

if __name__ == "__main__":
    linked_list = linked_list_from_array([1,2,3,4,5])
    print_linked_list(Solution().removeNthFromEnd(linked_list, 2)) # 
    linked_list = linked_list_from_array([1])
    print_linked_list(Solution().removeNthFromEnd(linked_list, 1)) # 
    linked_list = linked_list_from_array([1,2])
    print_linked_list(Solution().removeNthFromEnd(linked_list, 1)) # 
            