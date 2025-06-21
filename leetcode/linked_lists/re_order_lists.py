from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    s = ""
    seen = {}
    while current:
        if current in seen:
            break
        seen[current] = 1
        s += f"{current.val} - "
        current = current.next
    print(s)

def print_stack(stack):
    s = ""
    for el in stack:
        s += f"{el.val}-"
    print(s)

class Solution:

    def recursive(self, node):
        if node is None:
            return
        self.recursive(node.next)

        if self.stop:
            return

        if self.front == node or self.front.next == node:
            if self.front != node:
                self.front.next = node
            node.next = None
            self.stop = True
            return

        temp = self.front.next
        self.front.next = node
        node.next = temp
        self.front = temp


    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     self.front = head
    #     self.stop = False
    #     print('start')
    #     print_linked_list(head)
    #     self.recursive(head)
    #     print('end')
    #     print_linked_list(head)
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current = head
        stack = []
        while current:
            stack.append(current)
            current = current.next

        current = head
        seen = {}
        while current:
            seen[current] = 1
            temp = current.next
            new_next = stack.pop()
            if new_next in seen:
                current.next = None
                break
            if new_next == current:
                new_next.next= None
                break
            current.next = new_next
            new_next.next = temp
            current = temp
            seen[new_next] = 1