#!/env/python
#https://oj.leetcode.com/problems/sqrtx/

def sqrt(x):
    low = 0
    high = x
    
    while low <= high :
        mid = (low + high) / 2
        if mid * mid < x:
            low = mid + 1
        elif mid * mid == x:
            return mid
        else:
            high = mid - 1
    return high

def sqrt2(x):
    res = 1
    while not ((res * res < x)  and   (res + 1) * (res + 1)) > x and not (res * res == x):
        if res == 0:
            break
        last = res
        res = (x / last + last) / 2

    return res 
        
if __name__ == "__main__":
    print sqrt(2)
    print sqrt2(9)
