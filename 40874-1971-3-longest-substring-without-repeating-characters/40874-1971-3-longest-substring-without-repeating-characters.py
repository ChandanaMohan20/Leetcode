class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charset = set()
        start = 0
        maxlen = 0
        n = len(s)

        for i in range(n):
            while s[i] in charset:
                charset.remove(s[start])
                start+=1
            charset.add(s[i])
            maxlen = max(maxlen,i-start+1)

        return maxlen