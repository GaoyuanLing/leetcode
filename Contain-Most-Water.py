#/env/python
#https://oj.leetcode.com/problems/container-with-most-water/

def maxArea(heigh):
    high = len(heigh) - 1
    low = 0
    
    maxWater = 0
    while low < high:
        tmpWater = (high - low) * min(heigh[high], heigh[low])
        if tmpWater > maxWater:
            maxWater = tmpWater

        if heigh[low] < heigh[high]:
            heighLow = heigh[low]
            while heigh[low] <= heighLow and low < high:
                low += 1
        else:
            heighHigh = heigh[high]
            print heighHigh
            while heigh[high] <= heighHigh and high > low:
                high -= 1

    return maxWater

if __name__ == "__main__":
    print maxArea([4,6,2,6,7,11,2])

        
