#!/env/python
#https://oj.leetcode.com/problems/integer-to-roman/

def RomanToint(romStr):
    romDic = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    intDic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    res = 0
    location = 0
    lenRom = len(romStr)
    while location < lenRom and location + 2 < lenRom:
        if romStr[location + 1] in 'MDCLXV' and romStr[location: location + 2] in romDic:
            res += intDic[romDic.index(romStr[location: location + 2])]
            location += 2
        else:
            res += intDic[romDic.index(romStr[location])]
            location += 1
    print romStr[location:]
    if romStr[location: ] in romDic:
        res += intDic[romDic.index(romStr[location:])]
    else:
        res += intDic[romDic.index(romStr[location])] + intDic[romDic.index(romStr[location + 1])]
    print res

    return res
if __name__ == "__main__":
    print RomanToint("MMMCMXCIX")
    
