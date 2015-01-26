#!/env/python
#https://oj.leetcode.com/problems/swap-nodes-in-pairs/

def swapPairs(head):
    if head == None:
        return head
    p = head.next
    q = head
    if p == None:
        return head
    tmp = p.val
    p.val = q.val
    q.val = tmp

    if p.next != None and p.next.next != None:
        swapPairs(p.next)

    return head
