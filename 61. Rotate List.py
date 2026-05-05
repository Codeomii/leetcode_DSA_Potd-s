'''61. Rotate List:--

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109'''

# Solution:--

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0: return head
        
        cur, n = head, 1
        while cur.next:
            cur = cur.next
            n += 1
        
        k %= n
        if k == 0: return head
        
        cur.next = head 
        for _ in range(n - k):
            cur = cur.next
        
        new_head = cur.next
        cur.next = None
        return new_head