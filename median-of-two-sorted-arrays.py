#/env/python
#https://oj.leetcode.com/problems/median-of-two-sorted-arrays/

def findMedianSortedArray(A, B):
    la = len(A)
    lb = len(B)
    startA = 0
    startB = 0
    C = []
    median = 0
    while startA < la or startB < lb:
        if not A or not B:
            if not A:
                startB = lb
                C = B
            else:
                startA = la
                C = A
            break
        if startA < la and startB < lb:
            if A[startA] < B[startB]:
                C.append(A[startA])
                startA += 1
            else:
                C.append(B[startB])
                startB += 1
        elif startA < la or startB < lb:
            if startB < lb:
                C.append(B[startB])
                startB += 1
            else:
                C.append(A[startA])
                startA += 1
               
    lc = startA + startB
    if lc % 2:
        median = C[lc / 2]
    else:
        median = "%.5f"% ((C[lc / 2] + C[lc / 2 - 1]) / 2.0)
    return median

def findMedianSortedArray2(A, B):
    C = []
    for i in A:
        C.append(i)

    for i in B:
        C.append(i)

    C = sorted(C)
    lc = len(C)
    if lc % 2:
        median = C[lc / 2]
    else:
        median = "%.5f"% ((C[lc / 2] + C[lc / 2 - 1]) / 2.0)
    return median
    

if __name__ == "__main__":
    print findMedianSortedArray([], [2, 3])
    print findMedianSortedArray2([], [2, 3])
