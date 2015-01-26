#!/env/python
#https://oj.leetcode.com/problems/merge-two-sorted-lists/

def mergeTwoLists(l1, l2):
    head = ListNode(-1)
    t = head
    p = l1
    q = l2
    if not p:
        return q
    if not q:
        return p
    while p and q:
        if p.val < q.val:
            t.next = p
            p = p.next
        else:
            t.next = q
            q = q.next
        t = t.next

    if p:
        t.next = p
    if q:
        t.next = q

    return head.next

