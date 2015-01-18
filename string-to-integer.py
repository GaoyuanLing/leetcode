#!/env/python
#https://oj.leetcode.com/problems/string-to-integer-atoi/

def atoi(str):
    strToNum = {}
    maxInt = 2147483647
    minInt = -2147483648
    stringNum = "0123456789+- "
    if str == "":
        return 0
    for index in xrange(len(stringNum)):
        strToNum[stringNum[index]] = index

    if  str[0] not in strToNum:
        return 0

    syb = 1
    res = 0
    flag = False
    for index in xrange(len(str)):
        if str[index] in '+- ' and flag == True:
            break
        if str[index] == " ":
            continue
        if str[index] == '-':
            flag = True
            syb = -1
            continue
        if str[index] == '+':
            flag = True
            continue
        if str[index] not in strToNum:
            break
        res = res * 10 +  strToNum[str[index]]
        flag = True

    res = syb * res
    if res > maxInt:
        return maxInt
    if res < minInt:
        return minInt
    return res


if __name__ == "__main__":
    print atoi("123  456")
