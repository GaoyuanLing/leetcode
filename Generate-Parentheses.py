#/euv/python
#https://oj.leetcode.com/problems/generate-parentheses/

def generateParenthesis(n):
    res = []
    generate(n, n, "", res)
    return res

def generate(left, right, s, res):
    if left == 0 and right == 0:
        print s
        res.append(s)

    if left > 0:
        generate(left - 1, right, s + '(', res)

    if right > left and right > 0:
        generate(left, right - 1, s + ')', res)


if __name__ == "__main__":
    print generateParenthesis(3)
