#!/env/python
#https://oj.leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseGroup(self, head, k):
        realHead = ListNode(-1)
        realHead.next = head
        fakeHead = realHead
        while fakeHead:
            count = 0
            if not fakeHead.next:
                break
            p = fakeHead.next
            while p != None:
                p = p.next
                count += 1
            if count < k:
                break

            p = fakeHead.next
            count = 0
            fakeHead.next = None
            while p and count < k:
                tmp = p.next
                p.next = fakeHead.next
                fakeHead.next = p
                p = tmp
                count += 1

            count = 0
            while count < k:
                fakeHead = fakeHead.next
                count += 1
            fakeHead.next = tmp

        return realHead.next

if __name__ == "__main__":
    s = Solution()
    l = [1, 2, 3, 4]
    head = ListNode(-1)
    p = head
    for i in l:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    l = s.reverseGroup(p.next, 2)
    count = 0
    while l:
        count += 1
        print l.val
        l = l.next
