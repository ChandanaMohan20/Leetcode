class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        i=0
        while i<len(words)-1:
            sort1 = ''.join(sorted(words[i]))
            sort2 = ''.join(sorted(words[i+1]))
            
            if sort1 == sort2 :
                words.pop(i+1)
            else:
                i = i+1
        return words
                
        