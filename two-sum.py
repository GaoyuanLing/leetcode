#/env/python
#https://oj.leetcode.com/problems/two-sum/

def twoSum1(num, target):
    d = {}
    for i in xrange(len(num)):
        if num[i] not in d:
            d[num[i]] = [i + 1]
        else:
            d[num[i]].append(i + 1)

    print d
    for (k, v) in d.items():
        t = target - k
        if t in d:
            if t != k:
                if d[k] < d[t]:
                    return (d[k], d[t])
                else:
                    return (d[t], d[k])
            elif len(d[t]) >= 2:
                return (d[t][0], d[t][1])

def twoSum2(num, target):
    d = {}
    for i in xrange(len(num)):
        if target - num[i] in d:
            return (d[target - num[i]] + 1, i + 1)
        else:
            d[num[i]] = i

def twoSum3(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num), 1):
            if num[i] + num[j] == target:
                return (i + 1, j + 1)

def twoSum4(num, target):
    new = sorted(num)
    low = 0
    high = len(num) - 1
    while(low != high):
        if new[low] + new[high] > target:
            high -= 1
        elif new[low] + new[high] == target:
            return findIndex(new[low], new[high], num)
        else:
            low += 1
        
def findIndex(num1, num2, num):
    i = num.index(num1) + 1
    j = 0
    try:
        j = num.index(num2, 0, i - 1) + 1
    except:
        print len(num) - 1
        print i
        j = num.index(num2, i, len(num)) + 1
        pass

    print j
    print num2
    judge = (i > j)
    print judge
    return {False: (i,j), True: (j, i)}[judge]

if __name__ == "__main__":
    #print twoSum1([0, 4, 3, 0], 0)
    #print twoSum2([0, 4, 3, 0], 0)
    #print twoSum3([0, 4, 3, 0], 0)
    print twoSum4([5, 75, 25], 100)
