#/env/python
#https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
    

res = []
lenStr = 0
transLetter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
def letterCombinations(digits):
    global lenStr
    lenStr = len(digits)
    dfs(digits, 0, "")
    return res

def dfs(strArray, length, stradd):
    if length == lenStr:
        res.append(stradd)
        return res
  
    s = transLetter[strArray[length]]
    for i in s:
        dfs(strArray, length + 1, stradd + i)

if __name__ == "__main__":
    print letterCombinations("23")
