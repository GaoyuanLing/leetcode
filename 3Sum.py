#!/env/python
#https://oj.leetcode.com/problems/3sum/

def threeSum(num):
    if len(num) == 0:
        return []
    num = sorted(list(num))
   
    if num[0] > 0 or num[-1] < 0:
        return []

    result = []
    for i in xrange(len(num) - 2):
        left = i + 1
        right = len(num) - 1
        while left < right:
            sum = num[i] + num[left] + num[right]
            if sum == 0:
                if [num[i], num[left], num[right]] not in result:
                    result.append([num[i], num[left], num[right]])
                left += 1
                right -= 1
   
            if sum > 0:
                right -= 1

            if sum < 0:
                left += 1
    return result

def threeSum2(num):
    if len(num) == 0:
        return []
 
    hashset = [set(), set()]
    duplicate = set()
    result = []
    for element in num:
        if element == 0 and element in duplicate and len(result) == 0:
            result.append([0, 0, 0])
        
        if element >= 0:
            if element in hashset[0] and element not in duplicate:
                duplicate.add(element)
            elif element not in hashset[0]:
                hashset[0].add(element)

        else:
            if element in hashset[1] and element not in duplicate:
                duplicate.add(element)
            elif element not in hashset[1]:
                hashset[1].add(element)

        sortedList = [sorted(hashset[0]), sorted(hashset[1])]
     
    for x in xrange(len(sortedList[0])):
        if sortedList[0][x] in duplicate:
            if -2 * sortedList[0][x] in hashset[1]:
                result.append([-2 * sortedList[0][x], sortedList[0][x], sortedList[0][x]])
 
        for y in xrange(x + 1, len(sortedList[0])):
            if -(sortedList[0][x] + sortedList[0][y]) in hashset[1]:
                result.append([-(sortedList[0][x] + sortedList[0][y]), sortedList[0][x], sortedList[0][y]])
 
        
    for x in xrange(len(sortedList[1])):
        if sortedList[1][x] in duplicate:
            if -2 * sortedList[1][x] in hashset[0]:
                result.append([sortedList[1][x], sortedList[1][x], -2 * sortedList[1][x]])
 
        for y in xrange(x + 1, len(sortedList[1])):
            if -(sortedList[1][x] + sortedList[1][y]) in hashset[0]:
                result.append([sortedList[1][x], sortedList[1][y], -(sortedList[1][x] + sortedList[1][y])])

    return result

if __name__ == "__main__":
    print threeSum2([0,0,0])
    print threeSum2([-1, 0, 1])
