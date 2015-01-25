#/env/python
#https://oj.leetcode.com/problems/3sum-closest/

import sys

def threeSumClosest(num, target):
    closest = sys.maxint
    print closest
    num = sorted(num)
    for i in xrange(len(num)):
        low = i + 1
        high = len(num) - 1
        addNum = 0
        while low < high:
            addNum = num[i] + num[low] + num[high]
            if abs(addNum - target) < abs(closest - target):
                closest = addNum
            if addNum > target:
                high -= 1
            elif addNum == target:
                return target
            else:
                low += 1
    return closest

if __name__ == "__main__":
    print threeSumClosest([-1, 2, 1, -4], 1)
