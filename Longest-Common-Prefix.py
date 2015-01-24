#/env/pytho
#https://oj.leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    if strs == []:
        return ""
    if "" in strs:
        return ""
  
    comStr = strs[0]
    for sstr in strs[1:]:
        comIndex = 0
        lenCom = len(comStr)
        lenSstr = len(sstr)
        while comIndex < lenCom and comIndex < lenSstr and comStr[comIndex] == sstr[comIndex]:
            comIndex += 1
        if comIndex == 0:
            return ""
        comStr = comStr[0:comIndex]
    return comStr

if __name__ == "__main__":
    print longestCommonPrefix(['c', 'c'])
        
