#!/env/python
#https://oj.leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def insert(self, x):
        p = ListNode(x)
        p.next = self
        self = p
        return self

def addTwoNumber(l1, l2):
    num1 = l1.val
    l1 = l1.next
    n = 1
    while l1:
        num1 = num1 + l1.val * 10 * n
        n *= 10
        l1 = l1.next
    num2 = l2.val
    l2 = l2.next
    n = 1
    while l2:
        num2 = num2 + l2.val * 10
        n *= 10
        l2 = l2.next

    num = num1 + num2
    l0 = ListNode(num % 10)
    p = l0
    num = num / 10
    while num:
        t = ListNode(num % 10)
        num /= 10
        p.next = t
        p = p.next
    return l0

def addTwoNumber2(l1, l2):
    plusOne = 0
    l0 = ListNode(-1)
    p = l0
    while l1 or l2:
        if l1 and l2:
            val = l1.val + l2.val + plusOne
            if val >= 10:
                plusOne = 1
                val = val % 10
            else:
                plusOne = 0
            tmp = ListNode(val)
            l1 = l1.next
            l2 = l2.next
        elif l1:
            val = l1.val + plusOne
            if val >= 10:
                plusOne = 1
                val %= 10
            else:
                plusOne = 0
            tmp = ListNode(val)
            l1 = l1.next
        elif l2:
            val = l2.val + plusOne
            if val >= 10:
                plusOne = 1
                val %= 10
            else:
                plusOne = 0
            tmp = ListNode(val)
            l2 = l2.next
        p.next = tmp
        p = p.next
        
    if plusOne == 1:
        tmp = ListNode(1)
        p.next = tmp
    return l0.next 

if __name__ == "__main__":
    test1 = [9, 1, 6]
    test2 = [0]
    l1 = ListNode(test1[0])
    for i in test1[1:]:
        l1 = l1.insert(i)
    l2 = ListNode(test2[0])
    for i in test2[1:]:
        l2 = l2.insert(i)
    #print addTwoNumber(l1, l2).val
    print addTwoNumber2(l1, l2).val
