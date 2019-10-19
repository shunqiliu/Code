'''
92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
'''
My way:

Add 5 tags to remember the two nodes of head break,three node of inverse operation

be careful about the m=1 and n=last node, they will lead to exceed the index

The code are below
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
            f=ListNode(None)
            f.next=head
            pos=1
            if not head.next:
                return head
            while True :
                if pos==m:
                    he=f.next
                    h=f.next
                    ne=h.next
                    pre=ListNode(None)
                    while pos!=n+1:
                        h.next=pre
                        pre=h
                        h=ne
                        if ne:
                            ne=ne.next
                        pos+=1
                    f.next=pre
                    he.next=h
                    break
                pos+=1
                f=f.next
            if m==1:
                return f.next
            return head