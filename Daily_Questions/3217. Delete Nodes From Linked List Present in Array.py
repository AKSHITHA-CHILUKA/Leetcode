# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        # Step 1: Convert nums to a set for O(1) lookup
        num_set = set(nums)

        # Step 2: Create a dummy node pointing to head
        dummy = ListNode(0)
        dummy.next = head

        # Step 3: Use a pointer curr to traverse the list
        curr = dummy

        # Step 4: Traverse and remove nodes whose values are in num_set
        while curr.next:
            if curr.next.val in num_set:
                # Delete the node by skipping it
                curr.next = curr.next.next
            else:
                # Move to the next node
                curr = curr.next

        # Step 5: Return the modified list (skipping dummy node)
        return dummy.next
