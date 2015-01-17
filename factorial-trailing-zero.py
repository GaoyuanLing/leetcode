#~/env/python

# https://oj.leetcode.com/problems/factorial-trailing-zeroes/

def trailingZeros(n):
    count = 0
    mod = 5
    while n > mod:
        count = count + n / mod
        mod = mod * 5

    return count
    
if __name__ == "__main__":
    print trailingZeros(28)        
