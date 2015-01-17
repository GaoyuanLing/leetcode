#!/env/python

# https://oj.leetcode.com/problems/largest-number/

num = [1, 3, 9, 2, 8]

def selfcmp(a,b):
    return [1, -1][str(a) + str(b) > str(b) + str(a)]

num = sorted([str(l) for l in  num], cmp = selfcmp)

ans = "".join(num).lstrip('0')

print  ans or '0'
