from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        
        for s in strs:
            sortedstr = ''.join(sorted(s))
            result[sortedstr].append(s)
            sortedstr = ''
        return result.values()