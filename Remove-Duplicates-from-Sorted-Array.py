#!/env/python
#https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, A):
        if A == []:
            return 0
        if len(A) == 1:
            return 1
        count = 0
        dup = 0
        for i in xrange(1,len(A)):
            if A[i] == A[i - 1]:
                dup += 1
                continue
            else:
                count += 1
                A[i - dup] = A[i]

        return A[:len(A) - dup]

if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([1,1,2, 2, 2, 2,2 ])
