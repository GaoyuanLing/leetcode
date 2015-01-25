#/env/python
#https://oj.leetcode.com/problems/valid-parentheses/

def isValid(s):
    stack = []
    pushStack = '({['
    for i in s:
        if i in pushStack:
            stack.append(i)
        if i == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
        if i == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        if i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print isValid("}]}()){{)[{[(]")
