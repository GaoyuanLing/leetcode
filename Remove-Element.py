#!/env.python
#https://oj.leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, A, elem):
        if A == []:
            return 0
        start = 0
        count = 0
        while start < len(A):
            if A[start] == elem:
                start += 1
                count += 1
                continue
            else:
                A[start - count] = A[start]
                start += 1
        return len(A[:len(A) - count])
if __name__ == "__main__":
    s = Solution()
    print s.removeElement([4, 5], 4)
