#!/env/python
#https://oj.leetcode.com/problems/reverse-integer/

def reverse(x):
    symbol = True
    if x < 0:
        symbol = False
        x = -x
    ans = ""
    while x:
        ans += str(x % 10)
        x /= 10
        
    if ans:
        ans = int(ans)
    else:
        return 0
    if not symbol:
        ans = -ans
    return ans

if __name__ == "__main__":
    print reverse(1534236469)


    
