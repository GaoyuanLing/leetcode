#!/env/python
#https://oj.leetcode.com/problems/palindrome-number/

def isPalindrome(x):
    if x < 0:
        return False

    if x / 10 == 0:
        return True
    
    numToStr = {}
    desStr = "0123456789"
    numStr = []
    while x:
        numStr.append(x % 10)
        x = x / 10
    
    low = 0
    high = len(numStr) - 1
    isPali = True
    while(low < high):
        if numStr[low] != numStr[high]:
            isPali = False
            break
        low += 1
        high -= 1

    return isPali

if __name__ == "__main__":
    print isPalindrome(13454321)
