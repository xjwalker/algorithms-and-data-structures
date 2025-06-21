# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        current = head
        while current:
            seen[current] = 1
            if seen.get(current):
                return True
            current = current.next
        return False

if __name__ == "__main__":
    repeated = ListNode(3)
    f = ListNode(1)
    repeated.next = f
    print(Solution().hasCycle(f)) # True
    f = ListNode(1).next = ListNode(2).next = None
    print(Solution().hasCycle(f)) # False
            
