#/env/python
#https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        p = head
        q = head
        while n > 0:
            p = p.next
            n -= 1
        if p == None:
            return head.next
        while p.next != None:
            q = q.next
            p = p.next
        q.next = q.next.next
        return head

if __name__ == "__main__":
    s = Solution()
    l = [1, 2 ,3]
    flag = ListNode(-1)
    nextP = flag
    for i in l:
        tmp = ListNode(i)
        nextP.next = tmp
        nextP = tmp
    print s.removeNthFromEnd(flag.next, 1).val
