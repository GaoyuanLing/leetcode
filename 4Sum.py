#/env/python
#https://oj.leetcode.com/problems/4sum/

def fourSum(num, target):
    result = []
    num = sorted(num)
    for i in xrange(len(num) - 1):
        for j in xrange(i + 1, len(num)):
            low = j + 1
            high = len(num) - 1
            while low < high:
                if num[i] + num[j] + num[low] + num[high] == target:
                    result.append([num[i], num[j], num[low], num[high]])
                    high -= 1
                    low += 1
                elif num[i] + num[j] + num[low] + num[high] > target:
                    high -= 1
                else:
                    low += 1
    return result

def fourSum2(num, target):
    result = set()
    sumDic = {}
    for i in xrange(len(num)):
        for j in xrange(i + 1, len(num)):
            if num[i] + num[j] in sumDic:
                sumDic[num[i] + num[j]].append([i, j])
            else:
                sumDic[num[i] + num[j]] = [[i, j]]
   
    for i in xrange(len(num) - 3):
        for j in xrange(i + 1, len(num) - 2):
            minusNum = target - num[i] - num[j]
            if minusNum in sumDic:
                for numList in sumDic[minusNum]:
                    if numList[0] > j:
                        result.add(tuple(sorted([num[i], num[j], num[numList[0]], num[numList[1]]])))
    return [list(i) for i in result]

if __name__  == "__main__":
    print fourSum2([-5,5,4,-3,0,0,4,-2], 4)
