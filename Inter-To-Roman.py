#!/env/python
#https://oj.leetcode.com/problems/integer-to-roman/

def intToRoman(num):
    romDic = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    intDic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    stack = []
    for element in intDic:
        while num / element:
            stack.append(romDic[intDic.index(element)])
            num = num - element

    return ''.join(stack)

if __name__ == "__main__":
    print intToRoman(400)
    
