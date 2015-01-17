#!/env/python
#https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    index = 0
    maxlen = 0
    tmpk = 0
    tmpv = 0
    start = 0
    hashtb = [-1] * 260
    for i in xrange(len(s)):
        if i != start:
            hashtb[ord(s[i])] = -1
            continue
        if start != 0:
            hashtb[val] = j
        tmplen = index - start
        for j in xrange(index, len(s)):
            val = ord(s[j])
            if hashtb[val] != -1:
                start = hashtb[val] + 1
                hashtb[val] = -1
                hashtb[ord(s[i])] = -1
                tmpk = val
                tmpv = j
                index = j + 1
                break
            else:
                hashtb[val] = j
                tmplen += 1
        maxlen = max(maxlen, tmplen) 
    return maxlen          
     
if __name__ == "__main__":
    print lengthOfLongestSubstring("wlrbbmqbhcdarzowkk")
